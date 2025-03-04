# IP Address Display Applications

This repository contains simple Python web applications, built with the Flask framework, designed to display IP address information. You can use these applications to quickly determine the IPv4 and/or IPv6 addresses of clients accessing your web server.

## Applications

* **`ip_both.py` (Both IPv4 and IPv6):**
    * This application displays both the IPv4 and IPv6 addresses of the client.
    * It retrieves the IPv4 address from the `X-Real-IP` HTTP header.
    * It retrieves the IPv6 address from the `X-Forwarded-For` HTTP header.
    * It serves a JSON response containing both addresses.
* **`ip_v4.py` (IPv4 Only):**
    * This application displays only the IPv4 address of the client.
    * It retrieves the IPv4 address from the `X-Real-IP` HTTP header.
    * It serves a JSON response containing the IPv4 address.
* **`ip_v6.py` (IPv6 Only):**
    * This application displays only the IPv6 address of the client.
    * It retrieves the IPv6 address from the `X-Forwarded-For` HTTP header.
    * It serves a JSON response containing the IPv6 address.

## Technologies Used

* **Python:** The web applications are built using Python.
* **Flask:** A lightweight web framework for Python.

## Prerequisites

* Python 3.x

## Getting Started

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Flask applications:**

    ```bash
    python ip_both.py &
    python ip_v4.py &
    python ip_v6.py
    ```

    * These applications will run on ports 5000, 5001, and 5002, respectively.

5.  **Access the websites:**
    * Navigate to `http://127.0.0.1:5000`, `http://127.0.0.1:5001`, and `http://127.0.0.1:5002` in your web browser.

## Deployment Notes

* These applications are designed to be run behind a reverse proxy or load balancer. The IP address information is obtained from the `X-Real-IP` and `X-Forwarded-For` headers. Ensure that your reverse proxy is configured to pass these headers.
