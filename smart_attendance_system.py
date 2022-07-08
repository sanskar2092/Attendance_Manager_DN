import datetime
import sys
import os
import platform
import time
from decimal import Decimal
from threading import Thread

import cv2
import csv
import numpy as np
import pandas as pd
from PySide6 import QtGui, QtWidgets, QtCore
from PySide6.QtCore import QThread
from PIL import Image
from PySide6.QtWidgets import QLabel

from modules import *
from widgets import *
from pathlib import Path

os.environ["QT_FONT_DPI"] = "96"  # FIX Problem for High DPI and Scale above 100%
import time
import logging
import logging.handlers


def log_setup():
    log_handler = logging.handlers.WatchedFileHandler('my.log')
    formatter = logging.Formatter(
        '%(asctime)s program_name [%(process)d]: %(message)s',
        '%b %d %H:%M:%S')
    formatter.converter = time.gmtime  # if you want UTC time
    log_handler.setFormatter(formatter)
    logger = logging.getLogger()
    logger.addHandler(log_handler)
    logger.setLevel(logging.DEBUG)


log_setup()

# SET AS GLOBAL WIDGETS
widgets = None


class Resource:
    root_dir = os.path.dirname(__file__)

    def initialise_resources(self):
        # check directories
        for _dir in (
            self.student_details_dir,
            self.attendance_dir,
            self.training_data_dir,
        ):
            if self.dir_is_present(_dir):
                logging.debug(f"{_dir} directory present")
            else:
                os.makedirs(_dir)
                logging.debug(f"Created : {_dir} directory")
        if self.file_is_present(self.student_details):
            logging.debug(f"{self.student_details} is present")
        else:
            with open(
                self.student_details, "w", encoding="UTF8", newline=""
            ) as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(["Id", "Name"])
            logging.debug(f"Created : {self.student_details} directory")
        if self.file_is_present(self.trained_data_label):
            logging.debug(f"{self.trained_data_label} is present")
            widgets.home_title_label.setText("Smart Attendance System")
        else:
            widgets.home_title_label.setText(
                "Student registration data not available.\nPlease Register Students!"
            )
        if self.file_is_present(self.today_attendance_file_name):
            logging.debug(f"{self.today_attendance_file_name} is present")
        else:
            with open(
                self.today_attendance_file_name, "w", encoding="UTF8", newline=""
            ) as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(["Id", "Name", "Date", "Time"])
            logging.debug(f"Created : {self.today_attendance_file_name} attendance file")

    @property
    def today_attendance_file_name(self):
        return f"{self.attendance_dir}{os.sep}Attendance_{datetime.date.today().strftime('%Y-%m-%d')}.csv"

    def images_registered(self):
        if not (dir_present := self.dir_is_present(self.training_data_dir)):
            return False
        files = [
            _file for _file in os.listdir(self.training_data_dir) if "yml" not in _file
        ]
        return bool(len(files))

    def has_training_data(self):
        if self.file_is_present(self.trained_data_label):
            logging.debug(f"{self.trained_data_label} is present")
            return True
        else:
            logging.debug(f"{self.trained_data_label} is not present")
            return False

    def file_is_present(self, path_str) -> bool:
        path_obj = Path(path_str)
        return self.exists(path_str) and path_obj.is_file()

    def dir_is_present(self, path_str) -> bool:
        path_obj = Path(path_str)
        return self.exists(path_str) and path_obj.is_dir()

    @staticmethod
    def exists(path_str):
        try:
            path_obj = Path(path_str)
            my_abs_path = path_obj.resolve(strict=True)
        except FileNotFoundError:
            return False
        else:
            return True

    @property
    def resource_dir(self) -> str:
        return os.path.join(self.root_dir, "resources")

    @property
    def attendance_dir(self) -> str:
        return os.path.join(self.root_dir, "Attendance")

    @property
    def student_details_dir(self) -> str:
        return os.path.join(self.root_dir, "StudentDetails")

    @property
    def training_data_dir(self) -> str:
        return os.path.join(self.root_dir, "TrainingImage")

    @property
    def image_classifier(self) -> str:
        return f"{cv2.data.haarcascades}haarcascade_frontalface_default.xml"

    @property
    def trained_data_label(self) -> str:
        return os.path.join(self.training_data_dir, "trainer.yml")

    @property
    def student_details(self) -> str:
        return os.path.join(self.student_details_dir, "StudentDetails.csv")


class CameraThread(QThread):
    updateFrame = Signal(QImage)

    def __init__(self, parent=None):
        QThread.__init__(self, parent)
        self.status = False
        self.cam_feed = None
        self.resource = Resource()
        self.color = (10, 159, 255)
        self.border_width = 2
        self.minW = None
        self.minH = None

    @staticmethod
    def get_cam_feed_src():
        cv2.setUseOptimized(True)
        return cv2.VideoCapture(0, cv2.CAP_DSHOW)

    def run(self):
        if not self.valid_request():
            logging.warning("Invalid data to proceed further. Returning!")
            return
        self.cam_feed = self.get_cam_feed_src()
        self.cam_feed.set(3, 640)  # set video width
        self.cam_feed.set(4, 480)  # set video height
        # Define min window size to be recognized as a face
        self.minW = 0.1 * self.cam_feed.get(3)
        self.minH = 0.1 * self.cam_feed.get(4)
        self.status = True
        self.process_frame()

    def valid_request(self):
        pass

    def process_frame(self):
        pass

    def tear_down(self):
        pass

    @staticmethod
    def qt_image_frame(frame):
        # Reading the image in RGB to display it
        color_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Creating and scaling QImage
        h, w, ch = color_frame.shape
        img = QImage(color_frame.data, w, h, ch * w, QImage.Format_RGB888)
        scaled_img = img.scaled(640, 480, Qt.KeepAspectRatio)
        return scaled_img


class StudentRegisterFeedThread(CameraThread):
    def tear_down(self):
        logging.debug("tearing down setup for student registration")
        if self.status:
            self.status = False
            self.cam_feed.release()
            cv2.destroyAllWindows()
            logging.debug("resetting field values in registration page")
            widgets.register_live_feed.setText(
                f"{widgets.register_name_input.text().upper()}, registered successfully!\nPlease fill 'Student ID'\nand 'Student Name' followed by\n'Start Image Capture' button."
            )
            widgets.register_id_input.setText("")
            widgets.register_name_input.setText("")
            widgets.register_capture_button.setText(f"Registered {widgets.register_name_input.text()} !")
            logging.debug("terminating this thread")
            self.exit()
        widgets.register_live_feed.setText(
            "Please fill 'Student ID'\nand 'Student Name' followed by\n'Start Image Capture' button."
        )
        # Give time for the thread to finish
        logging.debug("sleep for 1 sec")
        time.sleep(1)

    def valid_request(self):
        if not (
            bool(widgets.register_id_input.text())
            and bool(widgets.register_name_input.text())
        ):
            widgets.register_live_feed.setText(
                "Please fill both 'Student ID'\nand 'Student Name' followed by\n'Start Image Capture' button."
            )
            return False
        return True

    def process_frame(self):
        _id, _name = (
            widgets.register_id_input.text(),
            widgets.register_name_input.text(),
        )
        widgets.register_capture_button.setEnabled(False)
        widgets.register_capture_button.setText(f'Registering {_name.split(" ")[0]} !')
        detector = cv2.CascadeClassifier(self.resource.image_classifier)
        sample_num = 0
        while self.status:
            ret, img = self.cam_feed.read()
            if not ret:
                continue
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(
                gray, 1.3, 5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE
            )
            for (x, y, w, h) in faces:
                cv2.rectangle(
                    img, (x, y), (x + w, y + h), self.color, self.border_width
                )
                # incrementing sample number
                sample_num += 1
                # saving the captured face in the dataset folder TrainingImage
                cv2.imwrite(
                    os.path.join(
                        self.resource.training_data_dir,
                        f"{_name}.{_id}.{sample_num}.jpg",
                    ),
                    gray[y : y + h, x : x + w],
                )
            # Emit signal
            self.updateFrame.emit(self.qt_image_frame(img))
            logging.info(f"sample count: {sample_num}, id: {_id}, name: {_name}")
            # wait for 2 milliseconds
            if cv2.waitKey(2) & 0xFF == ord("q"):
                break
            # break if the sample number is more than 100
            elif sample_num >= 100:
                break
        with open(
            self.resource.student_details, "a+", encoding="UTF8", newline=""
        ) as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow([_id, _name])
        logging.debug("Registration Successful")
        widgets.register_live_feed.setText(
            f"{widgets.register_name_input.text().upper()}, registered successfully!\nPlease fill 'Student ID'\nand 'Student Name' followed by\n'Start Image Capture' button."
        )
        self.tear_down()


class StudentAttendanceFeedThread(CameraThread):
    updateIDnName = Signal(list)

    @staticmethod
    def get_cam_feed_src():
        return cv2.VideoCapture(0, cv2.CAP_DSHOW)

    def tear_down(self):
        logging.debug("tearing down setup for student Attendance")
        if self.status:
            self.status = False
            self.cam_feed.release()
            cv2.destroyAllWindows()
            print("resetting field values in Attendance page")
            widgets.start_attendance_button.setEnabled(True)
            widgets.stop_attendance_button.setEnabled(False)
            widgets.attendance_last_result.setText(widgets.attendance_time_result_label.text())
            widgets.attendance_live_feed.setText("Click 'Start Attendance' !")
            logging.debug("terminating this thread")
            self.exit()
        widgets.attendance_live_feed.setText("Click 'Start Attendance' !")
        # Give time for the thread to finish
        logging.debug("sleep for 1 sec")
        time.sleep(1)

    def valid_request(self):
        if not self.resource.images_registered():
            msg = "Student registration data not available.\nPlease Register Students!"
            logging.debug(msg)
            widgets.attendance_live_feed.setText(msg)
            return False
        elif not self.resource.has_training_data():
            msg = "Face Recognition Model is not trained.\nPlease Train Image Model!"
            logging.debug(msg)
            widgets.attendance_live_feed.setText(msg)
            return False
        return True

    def process_frame(self):
        widgets.start_attendance_button.setEnabled(False)
        widgets.stop_attendance_button.setEnabled(True)
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read(self.resource.trained_data_label)
        face_cascade = cv2.CascadeClassifier(self.resource.image_classifier)
        df = pd.read_csv(self.resource.student_details)
        font = cv2.FONT_HERSHEY_SIMPLEX
        attendance_initial = pd.read_csv(self.resource.today_attendance_file_name)
        col_names = ["Id", "Name", "Date", "Time"]
        attendance = pd.DataFrame(columns=col_names)

        while self.status:
            ret, img = self.cam_feed.read()
            img = cv2.flip(img, 1)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(
                gray,
                1.2,
                5,
                minSize=(int(self.minW), int(self.minH)),
                flags=cv2.CASCADE_SCALE_IMAGE,
            )
            for (x, y, w, h) in faces:
                cv2.rectangle(
                    img, (x, y), (x + w, y + h), self.color, self.border_width
                )
                Id, conf = recognizer.predict(gray[y : y + h, x : x + w])

                if conf < 100:
                    aa = df.loc[df["Id"] == Id]["Name"].values
                    confstr = "  {0}%".format(round(100 - conf))
                    tt = str(Id) + "-" + aa

                else:
                    Id = "  Unknown  "
                    tt = str(Id)
                    confstr = "  {0}%".format(round(100 - conf))

                if (100 - conf) > 67:
                    ts = time.time()
                    date = datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d")
                    timeStamp = datetime.datetime.fromtimestamp(ts).strftime("%H:%M:%S")
                    aa = str(aa)[2:-2]
                    attendance.loc[len(attendance)] = [Id, aa, date, timeStamp]

                tt = str(tt)[2:-2]
                if (100 - conf) > 67:
                    tt = tt + " [Pass]"
                    cv2.putText(
                        img, str(tt), (x + 5, y - 5), font, 1, (255, 255, 255), 2
                    )
                    # Emit
                    attendance = attendance.drop_duplicates(subset=["Id", "Name"], keep="first")
                    self.updateIDnName.emit([Id, aa, attendance.shape[0]])
                else:
                    cv2.putText(
                        img, str(tt), (x + 5, y - 5), font, 1, (255, 255, 255), 2
                    )

                if (100 - conf) > 67:
                    cv2.putText(
                        img, str(confstr), (x + 5, y + h - 5), font, 1, (0, 255, 0), 1
                    )
                elif (100 - conf) > 50:
                    cv2.putText(
                        img, str(confstr), (x + 5, y + h - 5), font, 1, (0, 255, 255), 1
                    )
                else:
                    cv2.putText(
                        img, str(confstr), (x + 5, y + h - 5), font, 1, (0, 0, 255), 1
                    )

            # Emit signal
            self.updateFrame.emit(self.qt_image_frame(img))
            if cv2.waitKey(1) == ord("q"):
                break
        attendance_final = pd.concat([attendance, attendance_initial])
        attendance_final = attendance_final.drop_duplicates(subset=["Id"], keep="first")
        attendance_final.to_csv(self.resource.today_attendance_file_name, index=False)
        logging.debug("Attendance Successful")
        widgets.attendance_live_feed.setText("Click 'Start Attendance' !")
        self.tear_down()


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        self.resources = Resource()
        self.resources.initialise_resources()
        if (
            self.resources.images_registered()
            and not self.resources.has_training_data()
        ):
            self.start_model_training()

        title = "Smart Attendance System"
        self.setWindowTitle(title)

        UIFunctions.uiDefinitions(self)
        widgets.title_info.setText(title)
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))
        widgets.report_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )
        widgets.btn_home.clicked.connect(self.button_click_slot)
        widgets.btn_attendance.clicked.connect(self.button_click_slot)
        widgets.btn_register.clicked.connect(self.button_click_slot)
        widgets.btn_training.clicked.connect(self.button_click_slot)
        widgets.btn_report.clicked.connect(self.button_click_slot)
        widgets.stackedWidget.setCurrentWidget(widgets.home_panel)
        widgets.btn_home.setStyleSheet(
            UIFunctions.selectMenu(widgets.btn_home.styleSheet())
        )

        self.student_register_thread = StudentRegisterFeedThread(self)
        widgets.register_live_feed.setText(
            "Please fill both 'Student ID'\nand 'Student Name' followed by\n'Start Image Capture' button."
        )
        self.student_register_thread.updateFrame.connect(
            self.set_student_register_frame
        )
        widgets.register_capture_button.clicked.connect(
            self.student_register_thread.start
        )

        self.student_attendance_thread = StudentAttendanceFeedThread(self)
        widgets.attendance_live_feed.setText("Click 'Start Attendance' !")
        # Dynamic display date and time on the label in attendance page
        timer = QTimer(self)
        timer.timeout.connect(self.update_date_and_time)
        timer.start()
        self.student_attendance_thread.updateFrame.connect(
            self.set_student_attendance_frame
        )
        self.student_attendance_thread.updateIDnName.connect(
            self.update_attendance_name_and_id
        )
        widgets.start_attendance_button.clicked.connect(
            self.student_attendance_thread.start
        )
        widgets.stop_attendance_button.clicked.connect(
            self.student_attendance_thread.tear_down
        )

        widgets.start_training_button.clicked.connect(self.start_model_training)
        self.prepare_attendance_report()

        self.show()

    @staticmethod
    def update_date_and_time():
        _date = datetime.date.today().strftime('%d-%b-%Y')
        _time = datetime.datetime.now().strftime('%I:%M:%S %p')
        widgets.attendance_date_result_label.setText(_date)
        widgets.attendance_time_result_label.setText(_time)

    @Slot(list)
    def update_attendance_name_and_id(self, id_name_count):
        if id_name_count and len(id_name_count) == 3:
            _id, _name, _count = id_name_count[0], id_name_count[1], id_name_count[2]
            widgets.attendance_name_result_label.setText(str(_name))
            widgets.attendance_id_result_label.setText(str(_id))
            widgets.attendance_student_count_result.setText(str(_count))

    def button_click_slot(self):
        btn = self.sender()
        btn_name = btn.objectName()

        # SHOW HOME PAGE
        if btn_name == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home_panel)
            UIFunctions.resetStyle(self, btn_name)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW ATTENDANCE PAGE
        if btn_name == "btn_attendance":
            widgets.stackedWidget.setCurrentWidget(widgets.attendance_panel)
            UIFunctions.resetStyle(self, btn_name)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW REGISTER PAGE
        if btn_name == "btn_register":
            widgets.stackedWidget.setCurrentWidget(widgets.register_panel)
            UIFunctions.resetStyle(self, btn_name)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW TRAINING PAGE
        if btn_name == "btn_training":
            widgets.stackedWidget.setCurrentWidget(widgets.training_panel)
            UIFunctions.resetStyle(self, btn_name)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            widgets.training_text_label.setText(f"Click 'Start Model Training' !")

        # SHOW REPORTS PAGE
        if btn_name == "btn_report":
            widgets.stackedWidget.setCurrentWidget(widgets.reports_panel)
            UIFunctions.resetStyle(self, btn_name)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            self.prepare_attendance_report()

        # PRINT BTN NAME
        logging.debug(f'Button "{btn_name}" pressed!')

    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPosition().toPoint()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            logging.debug("Mouse click: LEFT CLICK")
        if event.buttons() == Qt.RightButton:
            logging.debug("Mouse click: RIGHT CLICK")

    @Slot(QImage)
    def set_student_register_frame(self, image):
        widgets.register_live_feed.setPixmap(QPixmap.fromImage(image))

    @Slot(QImage)
    def set_student_attendance_frame(self, image):
        widgets.attendance_live_feed.setPixmap(QPixmap.fromImage(image))

    def start_model_training(self):
        def getImagesAndLabels(path):
            # get the path of all the files in the folder
            imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
            # print(imagePaths)

            # create empth face list
            faces = []
            # create empty ID list
            Ids = []
            # now looping through all the image paths and loading the Ids and the images
            for imagePath in imagePaths:
                if "yml" in imagePath:
                    continue
                # loading the image and converting it to gray scale
                pilImage = Image.open(imagePath).convert("L")
                # Now we are converting the PIL image into numpy array
                imageNp = np.array(pilImage, "uint8")
                # getting the Id from the image
                Id = int(os.path.split(imagePath)[-1].split(".")[1])
                # extract the face from the training image sample
                faces.append(imageNp)
                Ids.append(Id)
            return faces, Ids

        # Optional, adds a counter for images trained
        def counter_img(path):
            imgcounter = 0
            imagePaths = [
                os.path.join(path, f) for f in os.listdir(path) if "yml" not in f
            ]
            for imagePath in imagePaths:
                logging.debug(rf"{str(imgcounter)} Images Trained \r")
                time.sleep(0.008)
                imgcounter += 1
                widgets.training_text_label.setText(
                    f"Model Training progress: {round(imgcounter/len(imagePath) * 100, 2)} % "
                )
            widgets.training_text_label.setText(
                f"Total Images used for training: {imgcounter}"
            )

        if not self.resources.images_registered():
            msg = "Student registration data not available.\nPlease Register Students!"
            logging.debug(msg)
            widgets.home_title_label.setText(msg)
            widgets.start_training_button.setText("Please\nRegister\nStudents!")
            return
        recognizer = cv2.face_LBPHFaceRecognizer.create()
        detector = cv2.CascadeClassifier(self.resources.image_classifier)
        faces, Id = getImagesAndLabels(self.resources.training_data_dir)
        Thread(target=recognizer.train(faces, np.array(Id))).start()
        # Below line is optional for a visual counter effect
        Thread(target=counter_img(self.resources.training_data_dir)).start()
        recognizer.save(self.resources.trained_data_label)
        logging.debug("All Images trained on model")
        widgets.home_title_label.setText("Smart Attendance System")

    def prepare_attendance_report(self):
        today_report_df = pd.read_csv(self.resources.today_attendance_file_name)
        today_report_df = today_report_df.reset_index()
        records_in_file = today_report_df.shape[0]
        app_table_record_count = widgets.report_table.rowCount()
        logging.debug(f"Records in app: {app_table_record_count}")
        logging.debug(f"Records in file: {records_in_file}")
        widgets.report_table.setRowCount(records_in_file)
        cols = ["Id", "Name", "Date", "Time"]
        for index, row_data in today_report_df.iterrows():
            logging.debug(f"{row_data['Id']}, {row_data['Name']}, {row_data['Date']}, {row_data['Time']}")
            for col in range(len(cols)):
                widgets.report_table.setItem(index, col, QTableWidgetItem(str(row_data[cols[col]])))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())
