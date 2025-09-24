-- Create the Clinic Database
CREATE DATABASE Clinic_Database


--Patient Table storing information about patients visiting the clinic.
CREATE TABLE Patients (
    patient_id INT PRIMARY KEY AUTO_INCREMENT, -- Unique ID for each patient
    first_name VARCHAR(50) NOT NULL,          -- Patient's first name
    last_name VARCHAR(50) NOT NULL,           -- Patient's last name
    date_of_birth DATE NOT NULL,              -- Patient's date of birth
    gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Gender of the patient
    phone VARCHAR(15) UNIQUE NOT NULL,        -- Unique contact 
    email VARCHAR(100) UNIQUE,                -- Email adress that is optional but needs to be unique
    address TEXT                              -- Home address of the patient
);

-- Specializations Table storing medical specialties that doctors can have.
CREATE TABLE Specializations (
    specialization_id INT PRIMARY KEY AUTO_INCREMENT, -- Unique ID for each specialization
    specialization_name VARCHAR(100) UNIQUE NOT NULL  -- Name of the specialization
);

--Doctors Table storing information about doctors working in the clinic.
--Each doctor belongs to one specialization (One-to-Many relationship with Specializations).
CREATE TABLE Doctors (
    doctor_id INT PRIMARY KEY AUTO_INCREMENT,     -- Unique ID for each doctor
    first_name VARCHAR(50) NOT NULL,             -- Doctor's first name
    last_name VARCHAR(50) NOT NULL,              -- Doctor's last name
    specialization_id INT NOT NULL,              -- Links to the doctor's specialization
    phone VARCHAR(15) UNIQUE NOT NULL,           -- Unique contact
    email VARCHAR(100) UNIQUE,                   -- Email adress that is optional but needs to be unique
    FOREIGN KEY (specialization_id) REFERENCES Specializations(specialization_id)
);

--Appointments Table tracks appointments between patients and doctors.
--Each appointment links one patient to one doctor.(one-to-one relationship)
CREATE TABLE Appointments (
    appointment_id INT PRIMARY KEY AUTO_INCREMENT, --Unique ID for each appointment
    patient_id INT NOT NULL,                        --Links to the patient
    doctor_id INT NOT NULL,                         --Links to the doctor
    appointment_date DATETIME NOT NULL,             --Scheduled date and time
    reason TEXT,                                    --Reason for the appointment
    status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled', --Appointment status
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id)
);

--Billing Table Storing billing information for each appointment.
CREATE TABLE Billing (
    bill_id INT PRIMARY KEY AUTO_INCREMENT,        --Unique ID for each bill
    appointment_id INT UNIQUE NOT NULL,            --Links to a specific appointment
    amount DECIMAL(10,2) NOT NULL,                --Amount to be paid
    payment_status ENUM('Pending', 'Paid', 'Cancelled') DEFAULT 'Pending', -- Payment status
    payment_date DATE,                             -- Date when payment was made
    FOREIGN KEY (appointment_id) REFERENCES Appointments(appointment_id)
);

--DoctorPatient Table
CREATE TABLE DoctorPatient (
    doctor_id INT NOT NULL,                        -- Links to the doctor
    patient_id INT NOT NULL,                       -- Links to the patient
    PRIMARY KEY (doctor_id, patient_id),           -- Composite primary key prevents duplicate pairs
    FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id),
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id)
);

