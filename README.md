```
____   ____                  .__                  _____          __                         __                
\   \ /   /___________  _____|__| ____   ____    /  _  \  __ ___/  |_  ____   _____ _____ _/  |_  ___________ 
 \   Y   // __ \_  __ \/  ___/  |/  _ \ /    \  /  /_\  \|  |  \   __\/  _ \ /     \\__  \\   __\/  _ \_  __ \
  \     /\  ___/|  | \/\___ \|  (  <_> )   |  \/    |    \  |  /|  | (  <_> )  Y Y  \/ __ \|  | (  <_> )  | \/
   \___/  \___  >__|  /____  >__|\____/|___|  /\____|__  /____/ |__|  \____/|__|_|  (____  /__|  \____/|__|   
              \/           \/               \/         \/                         \/     \/                   
```

# Cocoapods Version Automator

Este projeto foi desenvolvido visando facilitar o gerenciamento de Pods locais. Ele serve para 
automatizar o processo de gerar uma nova versão de um Pod: 

- Alterar o .podspec do Pod em si pela nova versão desejada 
- -> copiar o .podspec 
- -> criar uma pasta no stspec com o nome da nova versão do pod 
- -> colar o .podspec atualizado dentro da pasta.

Você pode fazer esse processo com quantas pods desejar de uma única vez. 

## Como instalar:

1. Clone o projeto para a sua $HOME
```commandline
git clone https://github.com/hugo-andreassa/CocoapodsVersionAutomator.git "$HOME/CocoapodsVersionAutomator"
```

2. Adicione a seguinte linha no seu PATH no .zshrc ou .bachrc (depedendo do bash que você estiver usando)
```commandline
$HOME/CocoapodsVersionAutomator/tools
```

3. Recarregue o seu bash para ele atualizar o PATH
```commandline
source .zshrc
```
ou 
```commandline
source .bashrc
```

Pronto! Agora você pode chamar o script usando ```versionAutomator``` de qualquer lugar do seu terminal.

## Usando o script:
Para usar o script você precisa passar 3 argumentos: 
- A pasta onde estão localizados os seus Pods locais;
- A pasta onde está localizado o seu STSpec;
- Os NOMES dos Pods que você quer atualizar (importante resaltar que é o nome do Pod, e não o nome da pasta do Pod).

Exemplo:
```commandline
versionAutomator -pP Pods/ -sP STSpec/ -p AFNetworking ORStackView SwiftyJSON
```

## Contribuições
Se estiver interessado em contribuir ou dar sugestões, dicas e melhorias, sinta-se a vontade para entrar em contato 
ou abrir um pull request! 


hugo.andreassa@gmail.com

