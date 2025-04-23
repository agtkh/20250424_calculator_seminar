#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: K.Agata
Date: 2025.04.d23
"""

import math
import random

if __name__ == "__main__":
    seed = random.randint(0, 2147483647)

    # モンテカルロ法を使って円周率の近似値を計算
    random.seed(seed)

    num_points = 10000000

    points_inside_circle = 0
    for _ in range(num_points):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance_squared = x**2 + y**2

        # 距離の2乗が1以下なら、点は円の内側にある
        if distance_squared <= 1:
            points_inside_circle += 1
    pi_estimate = 4.0 * points_inside_circle / num_points

    print(pi_estimate)
