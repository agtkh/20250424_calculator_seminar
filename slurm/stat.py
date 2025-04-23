
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: K.Agata
Date: 2025.04.d23         
"""

import os
import glob

def main():
    output_files = get_output_files(".")

    sum_val = 0.0
    count = 0
    for output_file in output_files:
        with open(output_file, 'r') as f:
            content = f.read()
        val = float(content)
        sum_val += val
        count += 1
    if count == 0:
        print("No output files found.")
        return
    avg_val = sum_val / count
    print(f"Average value: {avg_val}")


def get_output_files(output_dir):
    return glob.glob(os.path.join(output_dir, "*.out"))

if __name__ == "__main__":
    main()

