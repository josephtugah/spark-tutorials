
# Docker & WSL Setup Guide

This README provides instructions to install Docker and set up WSL (Windows Subsystem for Linux) on Windows, as well as Docker Desktop on macOS. 

## Prerequisites

Before beginning, ensure you have:
- **Windows 10/11** or **macOS 10.15 Catalina or later**.
- **Admin permissions** on your machine to install software.

---

## 1. Installation on Windows

### Step 1: Install WSL (Windows Subsystem for Linux)

1. **Enable WSL**: Open PowerShell as Administrator and run:
   ```powershell
   wsl --install
   ```
   This command installs the latest version of WSL, along with a default Linux distribution (usually Ubuntu).

2. **Install a Linux Distribution**: If you want a different distribution, you can install it via the Microsoft Store or specify it directly:
   ```powershell
   wsl --install -d <distribution_name>
   ```
   Example distributions include `Ubuntu`, `Debian`, and `Kali-Linux`.

3. **Update WSL Kernel**: If prompted, download and install the WSL kernel update package from [Microsoft’s official site](https://aka.ms/wsl2kernel).

4. **Set WSL Version to 2** (if not default):
   ```powershell
   wsl --set-default-version 2
   ```

### Step 2: Install Docker Desktop

1. **Download Docker Desktop** for Windows from the [Docker website](https://www.docker.com/products/docker-desktop).
2. Run the installer and follow the on-screen instructions.
3. During installation, ensure the option to enable WSL 2 is selected. Docker Desktop will use WSL 2 as its backend.
4. **Start Docker Desktop** and complete the setup. Docker Desktop should detect your WSL 2 installation and integrate with it.
5. **Test Docker Installation**: Open a WSL terminal (such as Ubuntu) and run:
   ```bash
   docker --version
   ```
   If Docker is correctly installed, it will display the Docker version.

---

## 2. Installation on macOS

1. **Download Docker Desktop** for macOS from the [Docker website](https://www.docker.com/products/docker-desktop).
2. Open the downloaded `.dmg` file and drag the Docker icon to the Applications folder.
3. Start Docker Desktop from Applications. It may prompt you to provide your password to complete the installation.
4. **Test Docker Installation**: Open a Terminal and run:
   ```bash
   docker --version
   ```
   If Docker is correctly installed, it will display the Docker version.

---

## Additional Notes

- **Windows Users**: WSL allows running Linux distributions and Docker seamlessly on Windows. Docker Desktop integrates with WSL to provide a native-like experience.
- **macOS Users**: macOS does not require WSL, so Docker Desktop will run directly on your system.

For further assistance, refer to Docker’s official [documentation](https://docs.docker.com/get-started/). Happy coding!
