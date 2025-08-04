# 📦 Projeto Integrado - Sistema de Estoque

Este projeto é um sistema de **gerenciamento de estoque** desenvolvido como parte do Projeto Integrado no curso de **Análise e Desenvolvimento de Sistemas**.  
Permite controlar produtos, entradas, saídas e organização física por localização.

> 🚀 Desenvolvido por [Mikael Alejandro](https://github.com/FoioMikael-apk)

---

## 🧰 Funcionalidades

- ✅ Cadastro de produtos (nome, descrição, quantidade, etc.)
- ➕ Adição e retirada de estoque
- 🗂️ Organização por localização (ex: corredor, rua, prateleira)
- 🔍 Busca e listagem de produtos em tempo real
- ✏️ Edição e exclusão de produtos
- 🧠 Armazenamento local com AsyncStorage
- 📱 Interface otimizada para celular e tablets

---

## 📸 Screenshots

<div align="center">
  <img src="https://github.com/user-attachments/assets/b7cf0666-4a7f-4622-97da-21ba8fc45aa3" width="220"/>
  <img src="https://github.com/user-attachments/assets/eaedf563-4f28-4f79-9825-0e97cffb5445" width="220"/>
  <img src="https://github.com/user-attachments/assets/9c3e54c0-7552-432a-96da-35e92e675ebb" width="220"/>
  <img src="https://github.com/user-attachments/assets/84b18c15-604e-45f6-8705-f2879349956d" width="220"/>
  <img src="https://github.com/user-attachments/assets/08879c79-f0d6-42da-8ba3-3c86291db977" width="220"/>
</div>

---

## 🛠️ Tecnologias Utilizadas

- **React Native**
- **Expo**
- **TypeScript**
- **AsyncStorage**
- **React Navigation**
- **React Native Paper**
- **React Native Vector Icons**

---

## ▶️ Como Rodar o Projeto

### Pré-requisitos

- Node.js (v18+)
- Expo CLI instalado globalmente:
```bash
npm install -g expo-cli
```

### Instruções

1. **Clone o repositório**
```bash
git clone https://github.com/FoioMikael-apk/ProjetoItegradoEstoque.git
cd ProjetoItegradoEstoque
```

2. **Instale as dependências**
```bash
yarn install
# ou
npm install
```

3. **Inicie o projeto**
```bash
npx expo start
# ou
expo start
```

4. **Visualize no celular**
- Escaneie o QR code com o app **Expo Go**
- Ou pressione `a` no terminal para abrir no emulador Android

---

## 🗂️ Estrutura do Projeto

```
ProjetoItegradoEstoque/
├── assets/               # Imagens e ícones
├── components/           # Botões, Cards, Inputs reutilizáveis
├── screens/              # Telas: Home, Estoque, CadastroProduto, etc.
├── storage/              # Lógica com AsyncStorage
├── App.tsx               # Ponto de entrada principal
└── ...
```

---

## 👨‍💻 Autor

**Mikael Alejandro**  
📧 [packmuvis@gmail.com](mailto:packmuvis@gmail.com)  
🔗 [github.com/FoioMikael-apk](https://github.com/FoioMikael-apk)

---

## 📘 Licença

Este é um projeto de cunho **educacional e autoral**.  
Uso permitido apenas com atribuição de créditos.

---

## 💡 Considerações Finais

Este sistema foi desenvolvido com foco em simplicidade e funcionalidade para controle de estoques em ambientes acadêmicos ou pequenos comércios. Contribuições e sugestões são bem-vindas!
