
# Histogram Equalization Project

## 🌍 Introduction

This project implements different histogram equalization techniques in various color spaces, including **Grayscale**, **LAB**, **HSV**, **YCbCr**, and **HSL**. The goal is to enhance the contrast of images by applying histogram equalization in different color spaces.

Each equalizer is designed using **Object-Oriented Programming (OOP)** principles, ensuring flexibility and extensibility.

---

## 🌟 Example Outputs

<h4 align="center">Original Image vs Processed Image Using Grayscale color space</h4>

<img src="Images/nature.jpg" width="400" /> <img src="Images/image_3_grayscale_output.jpg" width="400" />

<h4 align="center">Original Image vs Processed Image Using YCbCr color space</h4>

<img src="Images/stairs.jpg" width="400" /> <img src="Images/image_1_ycbcr_output.jpg" width="400" />

<h4 align="center">Original Image vs Processed Image Using HSV color space</h4>

<img src="Images/tokyo_night.jpg" width="400" /> <img src="Images/image_2_hsv_output.jpg" width="400" />

---
## ✨ Features
- **Grayscale** Histogram Equalization  
- **LAB** Histogram Equalization  
- **HSV** Histogram Equalization  
- **YCbCr** Histogram Equalization  
- **HSL** Histogram Equalization  
- **Interactive Command-Line Interface** — Select the image path and color space for equalization dynamically.  

---

## 🔧 Installation

### Requirements

Ensure you have **Python 3.10** or newer installed, then clone the repository and install the dependencies:

```bash
# Clone the repository
git clone https://github.com/Lion-sudo/Histogram-Equalizations.git

# Change the directory 
cd Histogram-Equalizations

# Install dependencies
pip install -r requirements.txt
```

The required libraries are:

- `opencv-python~=4.11.0.86`
- `numpy~=2.2.2`

---

## ⚡ Usage

Run the program with:

```bash
python histogram_equalization.py
```

### Step 1: Provide an image path

Once the program starts, you'll be prompted to enter the **path to the image** you wish to process:

```bash
Please provide the path to the image you want to use:
```

### Step 2: Choose a color space

After loading the image, select a histogram equalization method from the list:

```yaml
Choose the histogram equalization color space:
1: Grayscale
2: LAB
3: HSV
4: YCbCr
5: HSL
6: Exit the program
```

### Step 3: Continue or exit

After processing, you'll be asked whether you want to continue or exit the program:

```yaml
Would you like to continue or exit?
1: Continue using the current image
2: Load a new image
3: Exit the program
```

- If you choose **1**, you'll go back to Step 2 using the same image.
- If you choose **2**, you'll return to Step 1 to provide a new image path.
- If you choose **3**, the program will exit.

The program keeps running until you choose to exit.

### Output Image Naming Convention

The processed images will be saved in the project directory using the following naming format:  
`image_{input_image_number}_{color_space_used}.jpg`

Here:
- `{input_image_number}` refers to the number of the input image chosen by the user.
- `{color_space_used}` indicates the color space applied during histogram equalization (such as Grayscale, HSV, LAB, etc.).

For example:
- `image_1_hsv_output.jpg` means the output of the first image selected by the user, processed using **HSV** histogram equalization.

You can continue experimenting with different color spaces or process multiple images before exiting.

## 📁 Project Structure

- **`histogram_equalization.py`** — Main script for running the program.  
- **`equalizer_factory.py`** — Factory for creating histogram equalizer instances.  
- **EqualizerClasses/** — Folder containing all color space equalizer classes:  
  - `grayscale_histogram_equalizer.py`  
  - `lab_histogram_equalizer.py`  
  - `hsv_histogram_equalizer.py`  
  - `ycbcr_histogram_equalizer.py`  
  - `hsl_histogram_equalizer.py`  
  - `abstract_histogram_equalizer.py` (abstract base class)  
- **`requirements.txt`** — Lists the dependencies.  

---

## 🧑‍💻 Author

**Lion Abramov**  
GitHub: [Lion-sudo](https://github.com/Lion-sudo)  

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.  

