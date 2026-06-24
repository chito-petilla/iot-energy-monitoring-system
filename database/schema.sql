-- IoT Energy Monitoring System Database Schema

CREATE TABLE Devices (
    device_id VARCHAR(50) PRIMARY KEY,
    location VARCHAR(100),
    installed_date DATETIME
);

CREATE TABLE EnergyReadings (
    id INT IDENTITY(1,1) PRIMARY KEY,
    device_id VARCHAR(50),
    voltage FLOAT,
    current FLOAT,
    power FLOAT,
    timestamp DATETIME
);

CREATE TABLE EnergySummary (
    id INT IDENTITY(1,1) PRIMARY KEY,
    device_id VARCHAR(50),
    total_energy FLOAT,
    average_power FLOAT,
    recorded_date DATETIME
);

CREATE TABLE AuditLogs (
    id INT IDENTITY(1,1) PRIMARY KEY,
    action VARCHAR(100),
    timestamp DATETIME
);
