import sqlite3

con = sqlite3.connect('example.db')

cur = con.cursor()
# create student grades table
cur.execute('''-- Create the schema
CREATE TABLE Cursos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    CURSO TEXT,
    ATO_REGULATÓRIO TEXT,
    TURNO TEXT,
    VAGAS INTEGER
);''')
cur.execute('''
-- Insert the data
INSERT INTO Cursos (CURSO, ATO_REGULATÓRIO, TURNO, VAGAS) VALUES
('ADMINISTRAÇÃO', 'Portaria Nº 204, de 25/06/2020, DUO 07/07/2020.', 'NOTURNO', 60),
('BIOMEDICINA', 'Portaria Nº 109, de 04/02/2021, DUO 05/02/2021.', 'DIURNO', 40),
('BIOMEDICINA', 'Portaria Nº 109, de 04/02/2021, DUO 05/02/2021.', 'NOTURNO', 10),
('CIÊNCIAS CONTÁBEIS', 'Portaria Nº 204, de 25/06/2020, DUO 07/07/2020.', 'NOTURNO', 60),
('DIREITO', 'Portaria Nº 204, de 25/06/2020, DUO 07/07/2020.', 'DIURNO', 40),
('DIREITO', 'Portaria Nº 204, de 25/06/2020, DUO 07/07/2020.', 'NOTURNO', 40),
('EDUCAÇÃO FÍSICA (BACHARELADO)', 'Portaria Nº 135, de 05/06/2023, DUO 06/06/2023.', 'NOTURNO', 50),
('EDUCAÇÃO FÍSICA (LICENCIATURA)', 'Portaria Nº 150, de 21/06/2023, DUO 22/06/2023.', 'NOTURNO', 35),
('ENFERMAGEM', 'Portaria Nº 109, de 30/08/2021, DUO 31/08/2021.', 'DIURNO', 20),
('ENFERMAGEM', 'Portaria Nº 109, de 30/08/2021, DUO 31/08/2021.', 'NOTURNO', 15),
('FISIOTERAPIA', 'Portaria Nº 948, de 04/02/2021, DUO 05/02/2021.', 'DIURNO', 40),
('FISIOTERAPIA', 'Portaria Nº 948, de 04/02/2021, DUO 05/02/2021.', 'NOTURNO', 20),
('MEDICINA VETERINÁRIA', 'Portaria Nº 85, de 17/04/2023, DUO 18/04/2023.', 'DIURNO', 40),
('MEDICINA VETERINÁRIA', 'Portaria Nº 85, de 17/04/2023, DUO 18/04/2023.', 'NOTURNO', 20),
('ODONTOLOGIA', 'Portaria Nº 949, de 30/08/2021, DUO 31/08/2021.', 'DIURNO', 50),
('ODONTOLOGIA', 'Portaria Nº 949, de 30/08/2021, DUO 31/08/2021.', 'NOTURNO', 30),
('PSICOLOGIA', 'Portaria Nº 948, de 30/08/2021, DUO 31/08/2021.', 'DIURNO', 40),
('PSICOLOGIA', 'Portaria Nº 948, de 30/08/2021, DUO 31/08/2021.', 'NOTURNO', 50);

''')
# commit the changes
con.commit()

con.close()