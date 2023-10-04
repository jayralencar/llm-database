import sqlite3

con = sqlite3.connect('example.db')

cur = con.cursor()
# create student grades table
cur.execute('''CREATE TABLE Cronograma (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    DATAS TEXT,
    ATIVIDADES TEXT
);''')

# insert some data
cur.execute("""INSERT INTO Cronograma (DATAS, ATIVIDADES) VALUES
('23/06 a 23/07/2023', 'Realização de inscrições'),
('23/06 a 30/06/2023', 'Solicitação de isenção do pagamento da taxa de inscrição'),
('Até 11/07/2023', 'Divulgação das inscrições com isenção do pagamento da taxa de inscrição'),
('24/07/2023', 'Último prazo para pagamento da taxa - Não serão aceitos comprovantes de agendamento de pagamento'),
('28 a 30/07/2023', 'Prazo para envio do comprovante de pagamento no GRU no SIGRH, para pagamentos não reconhecidos automaticamente pelo SIGRH'),
('02/08/2023', 'Data provável para divulgação PRELIMINAR de candidatos inscritos'),
('03 e 04/08/2023', 'Interposição de recurso para inscrições indeferidas'),
('08/08/2023', 'Data provável para divulgação da relação DEFINITIVA de candidatos inscritos'),
('até 24/08/2023', 'Divulgação das Comissões Examinadoras, do cronograma de provas e lista de pontos a serem sorteados'),
('04 a 15/09/2023', 'Prazo para os candidatos enviarem Memorial/Plano de Trabalho/ou equivalente no SIGRH'),
('Até 22/09/2023', 'Prazo para que os candidatos enviem Memorial e Plano de Trabalho por meio do SIGRH, este último quando exigido nas informações Complementares da respectiva área de conhecimento para os candidatos que enviaram Memorial/Plano de Trabalho na Tabela acima'),
('De 25/09 a 20/10/2023', 'Período para realização das provas'),
('previsto 26/10/2023', 'Os cronogramas de provas de cada área serão divulgados individualmente pelos seus respectivos unidades acadêmicas e conterão o período de intervalo deste período'),
('dia útil subsequente à realização da Heteroidentificação', 'Resultado Preliminar Heteroidentificação'),
('até 30/11/2023', 'Resultado Definitivo Heteroidentificação'),
('até 30/11/2024', 'Publicação do resultado final no D.O.U.'),
('5 dias úteis subsequentes à publicação do Resultado Final no D.O.U.', 'Prazo para envio de recursos perante o CEPE');
""")
con.commit()

con.close()