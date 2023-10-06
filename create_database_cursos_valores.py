import sqlite3

con = sqlite3.connect('example.db')

cur = con.cursor()
# create student grades table
cur.execute("""-- Create the schema
CREATE TABLE CursoValores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Curso TEXT,
    Turno TEXT,
    Semestralidade TEXT,
    Mensalidade TEXT,
    Bônus_de_Pontualidade TEXT,
    Mensalidade_Até_o_Vencimento TEXT
);""")
cur.execute("""
-- Insert the data
INSERT INTO CursoValores (Curso, Turno, Semestralidade, Mensalidade, Bônus_de_Pontualidade, Mensalidade_Até_o_Vencimento) VALUES
('Administração', 'Noturno', 'R$ 8,037.12', 'R$ 1,339.52', 'R$ 187.53', 'R$ 1,151.99'),
('Biomedicina', 'Diurno e Noturno', 'R$ 13,704.42', 'R$ 2,284.07', 'R$ 228.41', 'R$ 2,055.66'),
('Ciências Contábeis', 'Noturno', 'R$ 7,271.70', 'R$ 1,211.95', 'R$ 169.67', 'R$ 1,042.28'),
('Direito', 'Diurno e Noturno', 'R$ 11,703.18', 'R$ 1,950.53', 'R$ 195.05', 'R$ 1,755.48'),
('Educação Física Bacharelado e Licenciatura', 'Diurno e Noturno', 'R$ 6,941.64', 'R$ 1,156.94', 'R$ 115.69', 'R$ 1,041.25'),
('Enfermagem', 'Diurno e Noturno', 'R$ 11,292.42', 'R$ 1,882.07', 'R$ 188.21', 'R$ 1,693.86'),
('Fisioterapia', 'Diurno e Noturno', 'R$ 13,079.28', 'R$ 2,179.88', 'R$ 217.99', 'R$ 1,961.89'),
('Medicina Veterinária', 'Diurno e Noturno', 'R$ 20,614.38', 'R$ 3,435.73', 'R$ 309.22', 'R$ 3,126.51'),
('Odontologia', 'Diurno e Noturno', 'R$ 24,243.60', 'R$ 4,040.60', 'R$ 404.06', 'R$ 3,636.54'),
('Psicologia', 'Diurno e Noturno', 'R$ 12,158.16', 'R$ 2,026.36', 'R$ 202.64', 'R$ 1,823.72');
""")
# commit the changes
con.commit()

con.close()