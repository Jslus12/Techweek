const mysql = require('mysql2');

// Configurações exatas para o seu Laragon
const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '', // Laragon vem sem senha por padrão
  database: 'teckweek_db' // Nome que você criou no passo anterior
});

connection.connect(err => {
  if (err) {
    console.error('Erro ao conectar: ' + err.stack);
    return;
  }
  console.log('Conectado ao MySQL com sucesso!');

  // Vamos ler os dados da sua tabela 'participantes'
  connection.query('SELECT * FROM participantes', (err, results) => {
    if (err) throw err;
    console.log('Dados encontrados no banco:');
    console.table(results); // Mostra em formato de tabelinha no terminal
    connection.end();
  });
});