# Custom Port Scanner with Service Detection

## https://github.com/poojithareddyrk-jpg/port-scanner-project.git 

## Team Members
1.Poojitha P - SRN:PES2UG24AM112
2. Leka N - SRN: PES2UG24AM082
3.Nakshathira- SRN:PES2UG24AM096

## 📖 Abstract

This mini project presents the design and implementation of a custom port scanner capable of identifying open TCP ports and detecting the services running on them. The primary goal of the project is to develop an efficient and user-friendly network scanning tool that combines low-level socket programming with an interactive interface for better visualization of results.

The scanner performs TCP-based port scanning over a specified range to determine whether ports are open or closed. To improve performance, concurrent scanning techniques are used to scan multiple ports simultaneously, significantly reducing overall scanning time. Once open ports are detected, banner grabbing is performed to extract service-related information such as HTTP, FTP, and SSH.

The results are displayed through a structured and interactive dashboard, allowing users to easily interpret the scan outcomes. The project demonstrates practical applications of networking concepts, socket programming, and basic cybersecurity techniques.

Overall, this work highlights the development of an efficient port scanning tool with improved performance and usability. Future enhancements may include advanced vulnerability detection, extended protocol support, and cloud-based deployment.

## Features
1.To develop a TCP-based port scanning mechanism that identifies open ports on a target host.
2.To implement concurrent scanning to improve performance and reduce scanning time.
3.To detect services running on open ports using banner grabbing techniques.
4.To present scan results through a user-friendly interface for easy understanding and analysis.

##  Technologies Used

- Python (Streamlit for frontend dashboard)  
- C++ (Core port scanning logic using sockets)  
- Socket Programming (TCP connections)  
- Multithreading (for concurrent scanning)  
- Pandas (for handling scan results)  

## How to Run

 1. Clone the repository
git clone https://github.com/your-username/port-scanner-project.git  
cd port-scanner-project  
2. Install dependencies
pip install -r requirements.txt  
3. Compile the C++ scanner
g++ scanner.cpp -o scanner  
4. Run the Streamlit app
streamlit run app.py  



##  How It Works

1. User inputs a target IP address and port range  
2. The scanner attempts TCP connections to each port  
3. Multiple ports are scanned simultaneously using concurrency  
4. Open ports are identified based on successful connections  
5. Banner grabbing is performed on open ports to detect services  
6. Results are processed and displayed in the Streamlit dashboard  

##  Future Improvements

- Implement continuous or real-time port monitoring to automatically detect newly opened ports without manual intervention  
- Add basic vulnerability detection for identified services  
- Deploy the application on cloud platforms (AWS/Azure)  
- Enhance visualization with advanced analytics  

## Disclaimer

This tool is intended for educational purposes only. Do not use it on networks or systems without proper authorization.
