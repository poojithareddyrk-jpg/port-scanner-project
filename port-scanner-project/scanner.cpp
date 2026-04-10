#include <iostream>
#include <string>
#include <cstring>
#include <unistd.h>
#include <arpa/inet.h>
#include <netdb.h>
#include <fstream>

using namespace std;

bool scanPort(string ip, int port, string &banner) {

    struct hostent* host = gethostbyname(ip.c_str());
    if (host == NULL) return false;

    for (int attempt = 0; attempt < 3; attempt++) {   // 🔁 retry loop

        int sock = socket(AF_INET, SOCK_STREAM, 0);
        if (sock < 0) continue;

        struct sockaddr_in target;
        target.sin_family = AF_INET;
        target.sin_port = htons(port);
        target.sin_addr = *(struct in_addr*)host->h_addr;

        struct timeval timeout;
        timeout.tv_sec = 0;
        timeout.tv_usec = 500000;

        setsockopt(sock, SOL_SOCKET, SO_RCVTIMEO, &timeout, sizeof(timeout));
        setsockopt(sock, SOL_SOCKET, SO_SNDTIMEO, &timeout, sizeof(timeout));

        int conn = connect(sock, (struct sockaddr*)&target, sizeof(target));

        if (conn == 0) {
            char buffer[1024] = {0};

            const char* msg = "HEAD / HTTP/1.0\r\n\r\n";
            send(sock, msg, strlen(msg), 0);

            int bytes = recv(sock, buffer, sizeof(buffer), 0);

            if (bytes > 0)
                banner = string(buffer);
            else
                banner = "No Banner";

            close(sock);
            return true;
        }

        close(sock);  // close before retry
    }

    return false;  // after all retries fail
}

int main(int argc, char* argv[]) {

    if (argc < 4) {
        cout << "Usage: ./scanner <ip> <start_port> <end_port>\n";
        return 1;
    }

    string ip = argv[1];
    int start = atoi(argv[2]);
    int end = atoi(argv[3]);

    ofstream file("results.csv");
    file << "Port,Status,Banner\n";

    for (int port = start; port <= end; port++) {

        string banner;

        if (scanPort(ip, port, banner)) {
            cout << "Port " << port << " OPEN\n";
            file << port << ",OPEN,\"" << banner << "\"\n";
        } else {
            file << port << ",CLOSED,-\n";
        }
    }

    file.close();

    cout << "\n✅ Scan Completed!\n";

    return 0;
}