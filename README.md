Asignación: CuentaBancaria
Objetivos
Practicar el escribir clases
Mientras seguimos pensando en nuestra aplicación bancaria, nos damos cuenta de que sería más preciso asignar un balance no al usuario directamente, sino que en el mundo real. Los usuarios tienen cuentas y las cuentas tienen balances. ¡Esto nos da la idea de que quizás una cuenta sea su propia clase! Pero como dijimos, no es completamente independiente de una clase; las cuentas solo existen porque los usuarios las abren.

Para esta tarea, no te preocupes por poner información de usuario en la clase CuentaBancaria. ¡Nos ocuparemos de eso en la próxima lección!

Primero, practiquemos un poco más la escritura de clases escribiendo una clase nueva CuentaBancaria.

La clase CuentaBancaria debe tener un balance. Cuando se crea una nueva instancia de CuentaBancaria, si se da un monto, el balance de la cuenta debe establecerse inicialmente en ese monto; de lo contrario, el balance debe comenzar en $0. La cuenta también debe tener una tasa de interés, guardada como decimal (es decir, 1% se guardaría como 0,01), que debe proporcionarse al crear la instancia. (Sugerencia: cuando se utilizan valores predeterminados en los parámetros, ¡el orden de los parámetros es importante!).

La clase también debe tener los siguientes métodos:


depósito(self, amount): aumenta el balance de la cuenta en el monto dado
retiro(self, amount): disminuye el balance de la cuenta en el monto dado si hay fondos suficientes; si no hay suficiente dinero, imprime el mensaje: "Fondos insuficientes: cobrando una tarifa de $5", y resta $5
mostrar_info_cuenta(self)imprime en la consola: por ejemplo, "Balance: $100"
generar_interés(self): aumenta el balance de la cuenta por el balance actual * la tasa de interés (siempre que el balance sea positivo) 
Esto significa que necesitamos una clase que se parezca a esto: +-*-/