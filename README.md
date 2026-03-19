# DevOps e SRE: Conceitos e Diferenças

## O que é DevOps?

DevOps é uma cultura e um conjunto de práticas que integra o desenvolvimento de software (Dev) e as operações de TI (Ops). O objetivo principal é encurtar o ciclo de vida do desenvolvimento de sistemas e fornecer entrega contínua com alta qualidade de software. DevOps foca em quebrar os silos entre as equipes para que elas trabalhem de forma unificada em todas as etapas, desde a concepção até a produção e o suporte.

**Exemplo:**
Uma equipe de desenvolvimento escreve o código para uma nova funcionalidade. Em um modelo tradicional, esse código seria repassado manualmente para a equipe de infraestrutura configurar e implantar. No DevOps, a equipe utiliza uma esteira de CI/CD (Integração e Entrega Contínuas). Quando o código é atualizado no repositório principal, testes automatizados são executados imediatamente. Se o código for aprovado, ele é automaticamente empacotado e implantado no ambiente de produção sem intervenção manual.

## O que é SRE (Site Reliability Engineering)?

SRE (Engenharia de Confiabilidade de Sites) é uma disciplina que aplica os princípios da engenharia de software para resolver problemas operacionais e de infraestrutura. A premissa fundamental do SRE é tratar as operações como um problema de software. O objetivo principal é criar sistemas altamente confiáveis e escaláveis, estabelecendo um equilíbrio matemático entre o lançamento de novas funcionalidades e a estabilidade operacional.

**Exemplo:**
Um SRE define que uma aplicação tem um SLO (Objetivo de Nível de Serviço) de 99,9% de disponibilidade no mês. Isso cria um "Error Budget" (Orçamento de Erro) de 0,1%, ou seja, o sistema tem uma margem de aproximadamente 43 minutos mensais permitidos para ficar fora do ar ou apresentar falhas. Se a equipe de desenvolvimento lança uma versão com bugs que consome esses 43 minutos na primeira semana, o lançamento de novas funcionalidades é bloqueado. A equipe inteira passa a focar exclusivamente em corrigir a estabilidade e a infraestrutura até o próximo ciclo.

## Diferenças Essenciais

* **Definição:** DevOps é a filosofia e a cultura (o "o quê"). SRE é uma forma específica e prescritiva de implementar DevOps utilizando práticas de engenharia de software (o "como").
* **Foco Operacional:** DevOps foca em velocidade de entrega e automação de processos. SRE foca em garantir a disponibilidade do sistema e gerenciar o risco operacional.
* **Métricas:** DevOps utiliza métricas voltadas ao ciclo de desenvolvimento, como frequência de deploy e tempo de recuperação (MTTR). SRE baseia-se em métricas de confiabilidade, como SLI (Indicadores), SLO (Objetivos), SLA (Acordos) e Error Budgets.


# Analisador Rápido de Textos

Este projeto consiste em uma aplicação web desenvolvida em Python utilizando o framework Streamlit. O objetivo principal do sistema é processar blocos de texto fornecidos pelo usuário e retornar métricas analíticas e estatísticas de forma instantânea.

## Funcionalidades

A aplicação realiza as seguintes operações no texto inserido:

* **Contagem de Caracteres e Palavras:** Calcula o volume total de caracteres (com e sem espaços) e o número total de palavras.
* **Estimativa de Tempo de Leitura:** Retorna o tempo médio estimado necessário para a leitura completa do texto, baseado em uma velocidade média de leitura.
* **Análise de Frequência de Termos:** Processa o texto para identificar as palavras mais utilizadas.
* **Visualização de Dados:** Gera um gráfico de barras nativo ilustrando a frequência das 5 palavras mais repetidas.

  


