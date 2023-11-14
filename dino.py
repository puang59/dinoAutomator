#!/usr/bin/env python3

import cv2
import numpy as np
import pyautogui

def capture_and_convert(region):
    screenshot = pyautogui.screenshot(region=region)
    return cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

def count_pixels(image, threshold):
    # counting the number of pixels in the image that have intensity values greater than the specified threshold.
    return np.sum(image > threshold)

def main():
    region_of_interest = (200, 600, 255, 250)
    threshold = 100

    while True:
        image = capture_and_convert(region_of_interest)

        black_pixel_count = count_pixels(image, threshold)
        white_pixel_count = count_pixels(image, threshold)

        print('Black pixels:', black_pixel_count)
        print('White pixels:', white_pixel_count)

        if 4000 < black_pixel_count < 30000 or 4000 < white_pixel_count < 30000:
            pyautogui.press('up')

        cv2.imshow('image', image)

if __name__ == "__main__":
    main()
