import streamlit as st
import pandas as pd
import socket
import matplotlib.pyplot as plt

# ---------------- SERVICE MAP ----------------
COMMON_SERVICES = {
    21: "FTP",
    22: "SSH",
    23: "TELNET",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP"
}

# ---------------- UI ----------------
st.set_page_config(page_title="Port Scanner", layout="centered")
st.title("🔥 Advanced Port Scanner Dashboard")

target = st.text_input("Enter Target IP", "127.0.0.1")

# ---------------- SCANNER WITH BANNER ----------------
def scan_port(ip, port):
    s = socket.socket()
    s.settimeout(0.5)

    try:
        s.connect((ip, port))
        
        banner = ""
        try:
            s.send(b"HEAD / HTTP/1.0\r\n\r\n")  # trigger response (for HTTP)
            banner = s.recv(1024).decode(errors="ignore").strip()
        except:
            banner = "No Banner"

        s.close()
        return "OPEN", banner

    except:
        return "CLOSED", "-"

# ---------------- BUTTON ----------------
if st.button("🚀 Scan Ports (1-100)"):

    results = []
    progress = st.progress(0)

    for port in range(1, 101):
        status, banner = scan_port(target, port)

        service = COMMON_SERVICES.get(port, "Unknown") if status == "OPEN" else "-"

        results.append({
            "Port": port,
            "Status": status,
            "Service": service,
            "Banner": banner
        })

        progress.progress(port)

    df = pd.DataFrame(results)

    st.success("✅ Scan Completed!")

    # ---------------- TABLE ----------------
    st.write("### 📊 Scan Results")
    st.dataframe(df)

    # ---------------- STATS ----------------
    open_ports = df[df["Status"] == "OPEN"].shape[0]
    closed_ports = df[df["Status"] == "CLOSED"].shape[0]

    st.write("### 📈 Summary")
    col1, col2 = st.columns(2)
    col1.metric("Open Ports", open_ports)
    col2.metric("Closed Ports", closed_ports)

    # ---------------- BAR CHART ----------------
    chart = pd.DataFrame({
        "Status": ["Open", "Closed"],
        "Count": [open_ports, closed_ports]
    }).set_index("Status")

    st.write("### 📊 Bar Chart")
    st.bar_chart(chart)

    # ---------------- PIE CHART ----------------
    st.write("### 🥧 Pie Chart")

    fig, ax = plt.subplots()
    ax.pie(chart["Count"], labels=chart.index, autopct='%1.1f%%')
    ax.set_title("Port Distribution")

    st.pyplot(fig)