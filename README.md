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
  <img src="https://github.com/user-attachments/assets/b0e1e20a-eecf-4e9e-8e0f-8fd6dc40b5cd" width="250"/>
  <img src="https://github.com/user-attachments/assets/3a841e85-8b18-49d4-9f23-fd8021c05ad3" width="250"/>
  <img src="https://github.com/user-attachments/assets/316f4982-1604-4573-9439-04d56dc46d11" width="250"/>
  <img src="https://github.com/user-attachments/assets/1226eb56-0fa4-4ad7-91d0-fc4d241f2bb8" width="250"/>
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
