from cuenta_bancaria import User

persona1 = User("CAROLA","muxeres@gmail.com")
persona1.hacer_deposito(400).hacer_deposito(200).hacer_deposito(100).hacer_retiro(300).mostrar_balance_usuario()


persona2 = User("Antonio","centauro@hotmail.com.br")
persona2.hacer_deposito(200).hacer_deposito(800).hacer_retiro(200).hacer_retiro(100).hacer_retiro(200).hacer_retiro(300).mostrar_balance_usuario()


