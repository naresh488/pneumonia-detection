# Pneumonia Detection Project

This project aims to develop a machine learning model for the detection of pneumonia from chest X-ray images. The model is trained using a dataset of labeled images and is evaluated on separate validation and test datasets.

## Project Structure

- **data/**: Contains the datasets used for training, validation, and testing the model.
  - **train/**: Directory containing the training dataset.
  - **val/**: Directory containing the validation dataset.
  - **test/**: Directory containing the test dataset.
  
- **notebooks/**: Contains Jupyter notebooks for model training and evaluation.
  - **Final review major pnemonia.ipynb**: Notebook with code for data preprocessing, model architecture, training, and visualization of results.

- **src/**: Contains the main application logic.
  - **app.py**: Python file for loading the model, making predictions, and serving the model.

- **requirements.txt**: Lists the Python dependencies required for the project.

## Setup Instructions

1. Clone the repository to your local machine:
   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```
   cd pneumonia-detection
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage Guidelines

- To train the model, open the Jupyter notebook `Final review major pnemonia.ipynb` and run the cells sequentially.
- To use the model for predictions, run the `app.py` script in the `src` directory.

## Acknowledgments

- This project utilizes various libraries and frameworks for machine learning and image processing. Please refer to the `requirements.txt` for a complete list of dependencies.