# Code Lanss

CodeLanss/
├── css/                  # Pasta para arquivos CSS (estilos em cascata).
│   ├── login.css         # Arquivo CSS com estilos específicos para a tela de login.
│   ├── reset.css         # Arquivo CSS para "resetar" os estilos padrão dos navegadores, garantindo consistência.
│   └── style.css         # Arquivo CSS principal para estilos gerais do site.
│
├── html/                 # Pasta para arquivos HTML.
│   ├── index.html        # Página HTML principal do site.
│   └── login.html        # Página HTML para login.
│
├── node_modules          # Pasta gerada pelo npm que armazena todas as dependências do projeto. Não deve ser editada ou enviada para controle de versão.
│
├── public/               # Contém arquivos estáticos que são servidos diretamente pelo servidor web.
│   ├── favicon.ico       # Ícone da aba do navegador.
│   ├── index.html        # Arquivo base da aplicação React. O código JavaScript é injetado aqui.
│   ├── logo192.png       # Logo da aplicação para ícones de atalho em telas pequenas.
│   ├── logo512.png       # Logo da aplicação para ícones de atalho em telas grandes.
│   ├── manifest.json     # Arquivo de configuração para Progressive Web Apps (PWAs).
│   └── robots.txt        # Arquivo que instrui os motores de busca sobre quais páginas do site devem ser rastreadas.
│
├── src/                  # Pasta com o código-fonte da aplicação (a parte mais importante do projeto).
│   ├── assets/           # Contém recursos estáticos como imagens, fontes e outros arquivos auxiliares.
│   │   └── logo.svg      # O logo da aplicação em formato de imagem vetorial.
│   ├── components/       # Onde ficam os componentes React reutilizáveis da sua interface.
│   ├── styles/           # Pasta para arquivos de estilo específicos da aplicação React, frequentemente usando pré-processadores.
│   │   ├── App.scss      # Estilos para o componente principal (App). Arquivo SCSS (Sass).
│   │   └── index.scss    # Estilos globais da aplicação. Arquivo SCSS (Sass).
│   ├── tests/            # Pasta para arquivos de testes automatizados da aplicação.
│   │   ├── App.test.ts   # Arquivo de teste para o componente App, escrito em TypeScript.
│   │   └── setupTest.ts  # Arquivo de configuração para o ambiente de testes.
│   ├── App.ts            # O componente principal da sua aplicação (escrito em TypeScript).
│   ├── index.ts          # O ponto de entrada da aplicação, onde o React é inicializado e renderiza o componente App.
│   └── react-app-env.d.ts# Arquivo de declaração de tipos para o ambiente React (TypeScript).
│
├── .gitignore            # Arquivo que lista os itens que o Git deve ignorar (ex: node_modules, arquivos de cache).
├── package-lock.json     # Garante que todos que instalam o projeto tenham as mesmas versões de dependências.
├── package.json          # Contém os metadados do projeto, dependências e scripts para rodar a aplicação.
├── README.md             # O arquivo de documentação principal do projeto, geralmente o primeiro a ser lido.
└── tsconfig.json         # Arquivo de configuração do TypeScript, definindo como o compilador deve funcionar.
```

---

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.
