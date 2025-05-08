# backend_test

Backend test with python

- ## Analyze the code present in the test

- ## What does this code do?

  El código recibe un evento donde este está compuesto por el Id del usuario y el Id del dispositivo.Con esta información, primero se obtiene el usuario y se valida si tiene uno de los roles suficientes para poder continuar con la operación. En caso de que la validación sea correcta, se obtiene el dispositivo por su Id, y luego con esa información se obtiene una lista de productos, donde al final estos se retornan junto a su valor.

- ## Which segments would you change, why?

  Cambiaría la parte de la asignación de los valores de products, products_width y flag, moviendo su inicialización a otro lugar para poder controlarlos de manera más sencilla y mantener el lambda_handler más limpio y centrado en su objetivo principal.Por último, también ajustaría la forma en la que se asignan los valores de los widths. En lugar de usar el índice i, utilizaría la función append() para seguir la misma lógica que se usa al construir el array de products, logrando así que todo el código sea más consistente entre sí.

- ## Could you make a better version?

  Sí, considero que aplicando los cambios que mencioné — como mover la inicialización de products, products_width y flag fuera del handler principal — se puede tener un mejor control del código y mantener el lambda_handler más enfocado en su lógica principal. Además, separar las funciones de obtención de datos en un archivo auxiliar también podría ser una buena mejora para mantener esta parte más limpia y organizada.

- ## Now do it and enjoy it
