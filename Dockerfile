# Use python base image
FROM python:3.9

# Set the working directory
WORKDIR /ld06_test

# Clone the repository
RUN git clone https://github.com/byq77/LIDAR_LD06_python_loder .

# Install the dependencies
RUN pip install -r requirements.txt

# Expose the necessary port
EXPOSE 8000

# Define the default command to run the app
CMD ["python3", "main.py", "--print"]