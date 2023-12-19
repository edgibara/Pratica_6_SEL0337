# Pratica_6_SEL0337
Resumo da Prática de Laboratório: Desenvolvimento de Projeto para Controle de Acesso com Raspberry Pi e Periféricos Embarcados

Introdução:
A prática introduz o uso de periféricos embarcados na Raspberry Pi, como módulo de câmera, tag RFID, aprendizado de máquina e controle de versão via Git/GitHub. O foco é estabelecer uma base para projetos de controle de acesso usando tags e reconhecimento facial em bancos de dados e servidores.

Conceitos Importantes:
Os conceitos fundamentais incluem OpenCV, PiCamera, visão computacional, Git/GitHub, RFID, banco de dados, web server, SPI (Serial Peripheral Interface) e machine learning.

Objetivo:
O objetivo principal da prática é desenvolver um projeto que sirva como base para controle de acesso por meio de tags e reconhecimento facial em sistemas embarcados. A comunicação SPI será utilizada com a tag RFID para controle de acesso, junto com o módulo de câmera na Raspberry Pi. O Git será empregado como sistema de versionamento, e o GitHub como repositório, incluindo histórico de versionamento.

Controle de Acesso via Tag:
O módulo RFID-MFRC522, operando em frequência HF (13,56 MHz até 5m), utiliza a tecnologia de identificação por radiofrequência. A comunicação com o sistema embarcado é feita via SPI, um protocolo de comunicação síncrona. O módulo é capaz de gravar informações nas tags, e a comunicação é estabelecida por linhas principais como MISO, MOSI, SCK e SS/CS.

Câmera e Reconhecimento Facial:
Para a parte da câmera, recomenda-se o uso da biblioteca OpenCV, com o método Haar Cascade, um algoritmo de machine learning que atua como classificador, buscando padrões faciais analisando a intensidade dos pixels em uma base de dados.

Git/GitHub:
O sistema de versionamento Git e o repositório GitHub são cruciais para a documentação e controle de versões do projeto. O Git lida com inconsistências e integra alterações no código feitas por diferentes partes do projeto. Repositórios no GitHub também servem como documentação para facilitar a implementação em outros projetos, promovendo a colaboração em grandes equipes.
