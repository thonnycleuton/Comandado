# Comandante
Comandante
Relatório técnico
Índice
1.	introdução	3
2.	domínio do problema	4
3.	requisitos funcionais	5
3.1	Identificação dos Atores do Sistema	5
3.1.1	<Ator 1>	5
3.1.2	<Ator 2>	5
3.2	Principais Casos de Uso	5
3.2.1	<Caso de Uso 1>	5
3.2.2	<Caso de Uso 2>	5
3.3	Modelo de Classes	6
3.3.1	Subsistema 1	6
Diagrama de Classes	6
Definições de Classes	6
Classe 1	6
Classe 2	6
3.3.2	Subsistema 2 …	6
4.	requisitos não-funcionais	7
4.1	Principais Restrições de Projeto	7
4.2	Requisitos Operacionais	7
4.3	Normas	7
5.	arquitetura do sistema	8
6.	projeto e implementação	9
6.1.1	Subsistema 1	9
Diagrama de Classes	9
Definições de Classes	9
Classe 1	9
Classe 2	9
7.	referências	10
8.	apêndices	11
8.1	Glossário	11
8.2	Lista de Casos de Uso	11
8.3	Dicionário de Classes	11

1. Introdução
Alguns Sistemas de Automação Comercial são desenhados para atender a um contexto geral e visa, quase sempre, a melhor normalização de processos que nem sempre atende os desejos de clientes. 
Visando uma clientela mais específica, o presente trabalho irá detalhar tecnicamente as soluções encontradas para automação de uma clínica de estética, sob um módulo de controle de Vendas de serviços, donde será feito o controle de Colaboradores, Serviços prestados, Clientes a própria venda do serviço e geração de relatórios de gesstão.
1. Domínio do Problema
Definir de forma breve o domínio do problema em que se enquadra o software.
Referir os principais conceitos envolvidos e apresentar o respectivo diagrama de classes resultante da fase de análise (apenas os conceitos do problema).
Figura 1. Modelo de Classes Simplificado (diagrama de classes muito simples, sem atributos e métodos, apenas os relacionamentos)
2. Requisitos Funcionais
Descrição textual e em diagrama dos principais requisitos funcionais do sistema, apresentados sob a forma de casos de utilização.
Figura 2. Visão geral do sistema (diagrama de casos de utilização simplificado)
2.1 Identificação dos Atores do Sistema
Identificação dos atores: perfis de utilização, aplicações relacionadas nas funcionalidades oferecidas pela aplicação e para os quais esta foi criada.
Figura 3. Atores do sistema (diagrama de casos de utilização só com os actores)
2.1.1 Cliente
Responsável pela contratação do serviço.
2.1.2 Usuários
Responsável por Operar os serviços, ligando-os a um cliente.
 1. Administrador – responsável por inserir, atualizar e deletar Clientes, Serviços, Usuários e Vendas;
 2. Recepcionista - responsável por abrir uma venda para o cliente;
 3. Atendentes – responsável por adicionar itens à venda de um cliente;
 4. Caixa – responsável por encerrar a venda e apresentar o valor consumido.
2.2 Principais Casos de Uso
2.2.1 <Efetuar Venda>

A venda é feita por um usuário registrado para um cliente previamente cadastrado. A venda é uma coleção de itens de serviços que podem ser escolhidos ao longo da estadia do cliente no estabelecimento.
Cada grupo de colaborador tem acesso somente a funções que lhe são cabidas.
Figura 4. <Caso de Uso 1> (diagrama de casos de uso  só com o caso em questão e eventuais casos de uso secundários, relacionados com este)

2.2.2 <Caso de Uso 2>
...
2.3 Modelo de Classes
A venda possui um fluxo bem definido, onde ela inicia-se com o usuario atendente criando a venda, o usuario atendente adicionando itens a esta venda e o usuario caixa finalizando a venda e recebendo o pagamento.
3. Requisitos Não-Funcionais
3.1 Principais Restrições de Projeto
Atendentes e Caixas acessam o sistema de vendas via Computador Desktop ou laptop.
Atendentes acessam o sistema por meio de Tablets ou smartphones.
3.2 Requisitos Operacionais
Exemplos de requisitos operacionais são:
Gestão de Configurações 
Gestão de Versões
Desempenho
Recuperação de Erros
Formação
Equipamentos
Suportes Lógicos
4. Arquitetura do Sistema
Descrição textual e em diagrama da arquitetura lógica e física do sistema. Justificar as opções tomadas.
Figura 5. Arquitetura Lógica (diagrama de classes com os subsistemas todos do sistema)

Figura 6. Arquitetura Fisica (diagrama de componentes e de distribuição do sistema)

5. Projeto e Implementação
Nesta seção, deve-se descrever as principais linhas orientadoras do desenho e implementação do sistema. É importante referir as opções de desenho tomadas e justificá-las de forma crítica (análise de prós e contras das principais alternativas).
Descrição das relações estáticas e dinâmicas entre as diversas classes do sistema. As classes podem ser agrupadas em packages. Diagramas de classes, atividades, estados e sequência, são diagramas típicos nesta secção do relatório.
Figura 7. Classe 1 (diagrama de classes global do sistema mas ainda com pouco detalhe)
5.1.1 Subsistema 1
Texto descritivo do subsistema 1  (package Java).
Diagrama de Classes
Breve leitura do diagrama de classes.
Figura 8. Subsistema 1 (diagrama de classes do subsistema)
Definições de Classes
Classe 1
Descrição detalhada da classe, da sua função no subsistema, das opções de implementação, dos atributos e métodos.
Classe 2
...

6. Referências
7. Apêndices
7.1 Glossário
Definições para cada um dos termos do domínio do problema, com indexação para os pontos principais onde são utilizados.
7.2 Lista de Casos de Uso
Lista de todos os casos de uso ordenados por ordem alfabética, com uma muito breve descrição e indexação para os pontos principais onde são utilizados.
7.3 Dicionário de Classes
Lista de todas as classes ordenadas por ordem alfabética, com uma muito breve descrição e indexação para os pontos principais onde são utilizados.
