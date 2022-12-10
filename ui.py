import cv2
import numpy as np
import pandas as pd
import pyautogui as pag
from dataclasses import dataclass, field
import time
import pyperclip
from enum import Enum


class BiasType(Enum):
    NoBias = 0
    CenterBias = 1
    WidthBias = 2
    HeightBias = 3


@dataclass
class CardConfig:
    template_file: str = None
    bias_type: BiasType = None


@dataclass
class CardLocationOutput:
    status: bool = False
    x: int = None
    y: int = None


class CardLocation:
    def __init__(self, config: CardConfig) -> None:
        self.config = config
        self.image_template = cv2.imread(self.config.template_file)
        self.template_shape = self.image_template.shape

    @property
    def get_location(self) -> CardLocationOutput:
        im1 = pag.screenshot()
        screenshot = np.array(im1)[:, :, ::-1].copy()
        resul2 = cv2.matchTemplate(
            self.image_template, screenshot, cv2.TM_SQDIFF_NORMED)

        min_dev, max_dev, min_loc, max_loc = cv2.minMaxLoc(resul2)

        if min_dev < 0.001:
            if self.config.bias_type == BiasType.NoBias:
                return CardLocationOutput(
                    status=True,
                    x=int(min_loc[0]),
                    y=int(min_loc[1])
                )
            if self.config.bias_type == BiasType.CenterBias:
                return CardLocationOutput(
                    status=True,
                    x=int(min_loc[0] + self.template_shape[0] / 2),
                    y=int(min_loc[1] + self.template_shape[1] / 2)
                )

            if self.config.bias_type == BiasType.WidthBias:
                return CardLocationOutput(
                    status=True,
                    x=int(min_loc[0] + self.template_shape[0] / 2),
                    y=int(min_loc[1])
                )
            if self.config.bias_type == BiasType.HeightBias:
                return CardLocationOutput(
                    status=True,
                    x=int(min_loc[0]),
                    y=int(min_loc[1] + self.template_shape[1] / 2)
                )

        else:
            return CardLocationOutput()

#
# class MentionLocation:
#     """
#     01 查看是否被艾特
#     """
#
#     def __init__(self) -> None:
#         self.mention_image_template = cv2.imread("images/image_01_mention.png")
#
#     @property
#     def get_mention_location(self) -> MentinOutput:
#         im1 = pag.screenshot()
#         openimage = np.array(im1)[:, :, ::-1].copy()
#         resul2 = cv2.matchTemplate(
#             self.mention_image_template, openimage, cv2.TM_SQDIFF_NORMED)
#
#         min_dev, max_dev, min_loc, max_loc = cv2.minMaxLoc(resul2)
#
#         if min_dev < 0.001:
#             return MentinOutput(
#                 status=True,
#                 x=int(min_loc[0]),
#                 y=int(min_loc[1])
#             )
#         else:
#             return MentinOutput()
#
#
# # ml = MentionLocation()
#
# # v = ml.get_mention_location
# # v
#
#
# @dataclass
# class UserTextOutput:
#     status: bool = False
#     x: int = 0
#     y: int = 0
#     # usertext:str = None
#
#
# class UserText:
#     """02 定位到对话位置"""
#
#     def __init__(self) -> None:
#         self.template_image = cv2.imread("images/image_02_usertextv2.png")
#         self.template_shape = self.template_image.shape
#
#     @property
#     def get_user_text_location(self) -> UserTextOutput:
#         im1 = pag.screenshot()
#         openimage = np.array(im1)[:, :, ::-1].copy()
#         resul2 = cv2.matchTemplate(self.template_image, openimage, cv2.TM_SQDIFF_NORMED)
#
#         min_dev, max_dev, min_loc, max_loc = cv2.minMaxLoc(resul2)
#
#         if min_dev < 0.001:
#             # pag.moveTo(x = min_loc[0] + self.template_shape[0]/2,
#             # y = min_loc[1] + self.template_shape[1]/2)
#             # pag.click(button='right')
#
#             return UserTextOutput(
#                 status=True,
#                 x=int(min_loc[0] + self.template_shape[0] / 2),
#                 y=int(min_loc[1] + self.template_shape[1] / 2)
#             )
#         else:
#             return UserTextOutput()
#
#
# @dataclass
# class CopyButtonOutput:
#     status: bool = False
#     x: int = 0
#     y: int = 0
#
#
# class CopyButton:
#     """03 找到复制按钮"""
#
#     def __init__(self) -> None:
#         self.template_image = cv2.imread("images/image_03_copy.png")
#
#     @property
#     def get_copy_location(self) -> CopyButtonOutput:
#         im1 = pag.screenshot()
#         openimage = np.array(im1)[:, :, ::-1].copy()
#         resul2 = cv2.matchTemplate(
#             self.template_image, openimage, cv2.TM_SQDIFF_NORMED)
#
#         min_dev, max_dev, min_loc, max_loc = cv2.minMaxLoc(resul2)
#
#         if min_dev < 0.001:
#             return CopyButtonOutput(
#                 status=True,
#                 x=int(min_loc[0]),
#                 y=int(min_loc[1])
#             )
#         else:
#             return CopyButtonOutput()
#
#
# @dataclass
# class InputTextOutput:
#     status: bool = False
#     x: int = 0
#     y: int = 0
#
#
# class InputText:
#     """
#     04 回复消息，获得文本输入框的位置
#     """
#
#     def __init__(self) -> None:
#         self.template_image = cv2.imread("images/image_04_input.png")
#         self.bias_shape = self.template_image.shape
#
#     @property
#     def get_location(self) -> InputTextOutput:
#         im1 = pag.screenshot()
#         openimage = np.array(im1)[:, :, ::-1].copy()
#         resul2 = cv2.matchTemplate(
#             self.template_image, openimage, cv2.TM_SQDIFF_NORMED)
#
#         min_dev, max_dev, min_loc, max_loc = cv2.minMaxLoc(resul2)
#
#         if min_dev < 0.001:
#             return InputTextOutput(
#                 status=True,
#                 x=int(min_loc[0]),
#                 y=int(min_loc[1] + self.bias_shape[1])
#             )
#         else:
#             return InputTextOutput()
#
#
# @dataclass
# class SendButtonOutput:
#     status: bool = False
#     x: int = 0
#     y: int = 0
#
#
# class SendButton:
#     """
#     06 获得【发送】按钮位置
#     """
#
#     def __init__(self) -> None:
#         self.template_image = cv2.imread("images/image_05_send.png")
#         # self.bias_shape = self.template_image.shape
#
#     @property
#     def get_location(self) -> SendButtonOutput:
#         im1 = pag.screenshot()
#         openimage = np.array(im1)[:, :, ::-1].copy()
#         resul2 = cv2.matchTemplate(
#             self.template_image, openimage, cv2.TM_SQDIFF_NORMED)
#
#         min_dev, max_dev, min_loc, max_loc = cv2.minMaxLoc(resul2)
#
#         if min_dev < 0.001:
#             return SendButtonOutput(
#                 status=True,
#                 x=int(min_loc[0]),
#                 y=int(min_loc[1])
#             )
#         else:
#             return SendButtonOutput()
