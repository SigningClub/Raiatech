-- phpMyAdmin SQL Dump
-- version 4.7.7
-- https://www.phpmyadmin.net/
--
-- Host: 179.188.16.47
-- Generation Time: 22-Mar-2022 às 22:47
-- Versão do servidor: 5.7.32-35-log
-- PHP Version: 5.6.40-0+deb8u12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `importdump`
--
CREATE DATABASE IF NOT EXISTS `importdump` DEFAULT CHARACTER SET latin1 COLLATE latin1_general_ci;
USE `importdump`;

-- --------------------------------------------------------

--
-- Estrutura da tabela `TB_ALO_Alternativas_Opcoes_RT`
--

CREATE TABLE `TB_ALO_Alternativas_Opcoes_RT` (
  `ALO_id_alternativa_opcao` bigint(20) NOT NULL,
  `ALO_enunciado_alternativa` varchar(200) COLLATE latin1_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `TB_AMS_Ambiente_Saber_RT`
--

CREATE TABLE `TB_AMS_Ambiente_Saber_RT` (
  `AMS_id_ambiente_saber` bigint(20) NOT NULL,
  `USR_id_email_usuario` varchar(100) COLLATE latin1_general_ci NOT NULL,
  `AMS_nome_ambiente_saber` varchar(50) COLLATE latin1_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `TB_BNC_Conteudos_BNCC_RT`
--

CREATE TABLE `TB_BNC_Conteudos_BNCC_RT` (
  `BNC_id_conteudo_bncc` bigint(20) NOT NULL,
  `DEN_id_disciplina_ensino` bigint(20) NOT NULL,
  `BNC_Ano` tinyint(4) NOT NULL,
  `BNC_Unidade_tematica` varchar(50) COLLATE latin1_general_ci NOT NULL,
  `BNC_Objeto_conhecimento` varchar(200) COLLATE latin1_general_ci NOT NULL,
  `BNC_Conteudo` varchar(200) COLLATE latin1_general_ci NOT NULL,
  `BNC_Expectativa_aprendizagem` varchar(200) COLLATE latin1_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `TB_DEN_Disciplinas_Ensino_RT`
--

CREATE TABLE `TB_DEN_Disciplinas_Ensino_RT` (
  `DEN_id_disciplina_ensino` bigint(20) NOT NULL,
  `DEN_nome_disciplina` varchar(100) COLLATE latin1_general_ci NOT NULL,
  `DEN_area_ensino` varchar(50) COLLATE latin1_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `TB_ELG_Elementos_Gamificacao_RT`
--

CREATE TABLE `TB_ELG_Elementos_Gamificacao_RT` (
  `ELG_id_elemento_gamificacao` bigint(20) NOT NULL,
  `ELG_descricao_elemento_gamificacao` varchar(100) COLLATE latin1_general_ci NOT NULL,
  `ELG_regras_elemento_gamificacao` varchar(200) COLLATE latin1_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `TB_LAT_Lancamentos_Atividades_RT`
--

CREATE TABLE `TB_LAT_Lancamentos_Atividades_RT` (
  `LAT_id_lancamento_atividade` bigint(20) NOT NULL,
  `ROA_id_roteiro_atividade` int(11) NOT NULL,
  `LAT_status_lancamento` char(1) COLLATE latin1_general_ci NOT NULL,
  `LAT_dt_hr_nicio_lancamento_atividade` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `TB_MOD_Modelos_3D_RT`
--

CREATE TABLE `TB_MOD_Modelos_3D_RT` (
  `MOD_id_modelo_3D` bigint(20) NOT NULL,
  `DEN_id_disciplina_ensino` bigint(20) NOT NULL,
  `BNC_id_conteudo_bncc` bigint(20) NOT NULL,
  `MOD_imagem_modelo_3D` longblob NOT NULL,
  `MOD_dt_criacao` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `TB_PLA_Planos_Assinatura_RT`
--

CREATE TABLE `TB_PLA_Planos_Assinatura_RT` (
  `USR_id_plano_assinatura` bigint(20) NOT NULL,
  `PLA_nome_plano` varchar(50) COLLATE latin1_general_ci NOT NULL,
  `PLA_valor_plano` decimal(5,2) NOT NULL,
  `PLA_atributos_plano` varchar(150) COLLATE latin1_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `TB_QAL_Questoes_Alternativas_RT`
--

CREATE TABLE `TB_QAL_Questoes_Alternativas_RT` (
  `QAT_id_questao_atividade` bigint(20) NOT NULL,
  `ALO_id_alternativa_opcao` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `TB_QAT_Questoes_Atividades_RT`
--

CREATE TABLE `TB_QAT_Questoes_Atividades_RT` (
  `QAT_id_questao_atividade` bigint(20) NOT NULL,
  `MOD_id_modelo_3D` bigint(20) NOT NULL,
  `QAT_tipo_questao` char(1) COLLATE latin1_general_ci NOT NULL,
  `QAT_enunciado_questao` varchar(200) COLLATE latin1_general_ci NOT NULL,
  `QAT_comando_questao` varchar(100) COLLATE latin1_general_ci NOT NULL,
  `QAT_id_alternativa_questao_correta` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `TB_QEG_Questoes_Elementos_Gamificacao_RT`
--

CREATE TABLE `TB_QEG_Questoes_Elementos_Gamificacao_RT` (
  `ELG_id_elemento_gamificacao` bigint(20) NOT NULL,
  `QAT_id_questao_atividade` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `TB_QRT_Questoes_Roteiros_RT`
--

CREATE TABLE `TB_QRT_Questoes_Roteiros_RT` (
  `ROA_id_roteiro_atividade` bigint(20) NOT NULL,
  `QAT_id_questao_atividade` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `TB_RAU_Ranking_Usuario_RT`
--

CREATE TABLE `TB_RAU_Ranking_Usuario_RT` (
  `USR_id_email_usuario` varchar(100) COLLATE latin1_general_ci NOT NULL,
  `RAU_pontuacao_usuario` int(11) NOT NULL,
  `RAU_nivel_usuario` tinyint(4) NOT NULL,
  `RAU_coins_usuario` mediumint(9) NOT NULL,
  `RAU_trofeus_usuario` tinyint(4) NOT NULL,
  `RAU_medalhas_usuario` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `TB_RLA_Resultados_Lançamento_Atividade_RT`
--

CREATE TABLE `TB_RLA_Resultados_Lançamento_Atividade_RT` (
  `RLA_id_lancamento_atividade` bigint(20) NOT NULL,
  `USR_id_email_usuario` varchar(100) COLLATE latin1_general_ci NOT NULL,
  `QAT_id_questao_atividade` int(11) NOT NULL,
  `RLA_id_alternativa_questao_resposta` int(11) NOT NULL,
  `RLA_dt_hr_resultado_atividade` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `TB_ROA_Roteiros_Atrividades_RT`
--

CREATE TABLE `TB_ROA_Roteiros_Atrividades_RT` (
  `ROA_id_roteiro_atividade` int(11) NOT NULL,
  `AMS_id_ambiente_saber` int(11) NOT NULL,
  `USR_id_email_usuario` varchar(100) COLLATE latin1_general_ci NOT NULL,
  `ROA_nome_roteiro_atividade` varchar(50) COLLATE latin1_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `TB_TPU_Tipo_Usuario_RT`
--

CREATE TABLE `TB_TPU_Tipo_Usuario_RT` (
  `TPU_cod_tipo_usuario` bigint(20) NOT NULL,
  `TPU_descricao_tipo_usuario` varchar(50) COLLATE latin1_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `TB_USP_Usuarios_Planos_RT`
--

CREATE TABLE `TB_USP_Usuarios_Planos_RT` (
  `PLA_id_plano_assinatura` bigint(20) NOT NULL,
  `USR_id_email_usuario` varchar(100) COLLATE latin1_general_ci NOT NULL,
  `USP_dt_hr_ativacao_plano` datetime NOT NULL,
  `USP_status_plano` char(1) COLLATE latin1_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `TB_USR_Usuarios_RT`
--

CREATE TABLE `TB_USR_Usuarios_RT` (
  `USR_id_email_usuario` varchar(100) COLLATE latin1_general_ci NOT NULL,
  `USR_nome_usuario` varchar(50) COLLATE latin1_general_ci NOT NULL,
  `USR_senha_usuario` varchar(255) COLLATE latin1_general_ci NOT NULL,
  `TPU_cod_tipo_usuario` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

-- --------------------------------------------------------
--
--
-- Indexes for dumped tables
--

--
-- Indexes for table `TB_ALO_Alternativas_Opcoes_RT`
--
ALTER TABLE `TB_ALO_Alternativas_Opcoes_RT`
  ADD PRIMARY KEY (`ALO_id_alternativa_opcao`);

--
-- Indexes for table `TB_AMS_Ambiente_Saber_RT`
--
ALTER TABLE `TB_AMS_Ambiente_Saber_RT`
  ADD PRIMARY KEY (`AMS_id_ambiente_saber`),
  ADD KEY `USR_id_email_usuario` (`USR_id_email_usuario`);

--
-- Indexes for table `TB_BNC_Conteudos_BNCC_RT`
--
ALTER TABLE `TB_BNC_Conteudos_BNCC_RT`
  ADD PRIMARY KEY (`BNC_id_conteudo_bncc`),
  ADD KEY `DEN_id_disciplina_ensino` (`DEN_id_disciplina_ensino`);

--
-- Indexes for table `TB_DEN_Disciplinas_Ensino_RT`
--
ALTER TABLE `TB_DEN_Disciplinas_Ensino_RT`
  ADD PRIMARY KEY (`DEN_id_disciplina_ensino`);

--
-- Indexes for table `TB_ELG_Elementos_Gamificacao_RT`
--
ALTER TABLE `TB_ELG_Elementos_Gamificacao_RT`
  ADD PRIMARY KEY (`ELG_id_elemento_gamificacao`);

--
-- Indexes for table `TB_LAT_Lancamentos_Atividades_RT`
--
ALTER TABLE `TB_LAT_Lancamentos_Atividades_RT`
  ADD KEY `ROA_id_roteiro_atividade` (`ROA_id_roteiro_atividade`);

--
-- Indexes for table `TB_MOD_Modelos_3D_RT`
--
ALTER TABLE `TB_MOD_Modelos_3D_RT`
  ADD PRIMARY KEY (`MOD_id_modelo_3D`),
  ADD KEY `DEN_id_disciplina_ensino` (`DEN_id_disciplina_ensino`);

--
-- Indexes for table `TB_PLA_Planos_Assinatura_RT`
--
ALTER TABLE `TB_PLA_Planos_Assinatura_RT`
  ADD PRIMARY KEY (`USR_id_plano_assinatura`);

--
-- Indexes for table `TB_QAL_Questoes_Alternativas_RT`
--
ALTER TABLE `TB_QAL_Questoes_Alternativas_RT`
  ADD KEY `QAT_id_questao_atividade` (`QAT_id_questao_atividade`),
  ADD KEY `ALO_id_alternativa_opcao` (`ALO_id_alternativa_opcao`);

--
-- Indexes for table `TB_QAT_Questoes_Atividades_RT`
--
ALTER TABLE `TB_QAT_Questoes_Atividades_RT`
  ADD PRIMARY KEY (`QAT_id_questao_atividade`),
  ADD KEY `MOD_id_modelo_3D` (`MOD_id_modelo_3D`);

--
-- Indexes for table `TB_QRT_Questoes_Roteiros_RT`
--
ALTER TABLE `TB_QRT_Questoes_Roteiros_RT`
  ADD KEY `QAT_id_questao_atividade` (`QAT_id_questao_atividade`);

--
-- Indexes for table `TB_RAU_Ranking_Usuario_RT`
--
ALTER TABLE `TB_RAU_Ranking_Usuario_RT`
  ADD KEY `id_email_usuario` (`USR_id_email_usuario`);

--
-- Indexes for table `TB_RLA_Resultados_Lançamento_Atividade_RT`
--
ALTER TABLE `TB_RLA_Resultados_Lançamento_Atividade_RT`
  ADD PRIMARY KEY (`RLA_id_lancamento_atividade`);

--
-- Indexes for table `TB_ROA_Roteiros_Atrividades_RT`
--
ALTER TABLE `TB_ROA_Roteiros_Atrividades_RT`
  ADD PRIMARY KEY (`ROA_id_roteiro_atividade`),
  ADD KEY `USR_id_email_usuario` (`USR_id_email_usuario`);

--
-- Indexes for table `TB_TPU_Tipo_Usuario_RT`
--
ALTER TABLE `TB_TPU_Tipo_Usuario_RT`
  ADD PRIMARY KEY (`TPU_cod_tipo_usuario`);

--
-- Indexes for table `TB_USP_Usuarios_Planos_RT`
--
ALTER TABLE `TB_USP_Usuarios_Planos_RT`
  ADD KEY `USR_id_email_usuario` (`USR_id_email_usuario`) USING BTREE,
  ADD KEY `PLA_id_plano_assinatura` (`PLA_id_plano_assinatura`) USING BTREE;

--
-- Indexes for table `TB_USR_Usuarios_RT`
--
ALTER TABLE `TB_USR_Usuarios_RT`
  ADD KEY `USR_email_usuario_RT` (`USR_id_email_usuario`) USING BTREE,
  ADD KEY `TPU_cod_tipo_usuario` (`TPU_cod_tipo_usuario`) USING BTREE;

--
-- Limitadores para a tabela `TB_AMS_Ambiente_Saber_RT`
--
ALTER TABLE `TB_AMS_Ambiente_Saber_RT`
  ADD CONSTRAINT `TB_AMS_Ambiente_Saber_RT_ibfk_1` FOREIGN KEY (`USR_id_email_usuario`) REFERENCES `TB_USR_Usuarios_RT` (`USR_id_email_usuario`);

--
-- Limitadores para a tabela `TB_BNC_Conteudos_BNCC_RT`
--
ALTER TABLE `TB_BNC_Conteudos_BNCC_RT`
  ADD CONSTRAINT `TB_BNC_Conteudos_BNCC_RT_ibfk_1` FOREIGN KEY (`DEN_id_disciplina_ensino`) REFERENCES `TB_DEN_Disciplinas_Ensino_RT` (`DEN_id_disciplina_ensino`);

--
-- Limitadores para a tabela `TB_LAT_Lancamentos_Atividades_RT`
--
ALTER TABLE `TB_LAT_Lancamentos_Atividades_RT`
  ADD CONSTRAINT `TB_LAT_Lancamentos_Atividades_RT_ibfk_1` FOREIGN KEY (`ROA_id_roteiro_atividade`) REFERENCES `TB_ROA_Roteiros_Atrividades_RT` (`ROA_id_roteiro_atividade`);

--
-- Limitadores para a tabela `TB_MOD_Modelos_3D_RT`
--
ALTER TABLE `TB_MOD_Modelos_3D_RT`
  ADD CONSTRAINT `TB_MOD_Modelos_3D_RT_ibfk_1` FOREIGN KEY (`DEN_id_disciplina_ensino`) REFERENCES `TB_DEN_Disciplinas_Ensino_RT` (`DEN_id_disciplina_ensino`);

--
-- Limitadores para a tabela `TB_QAL_Questoes_Alternativas_RT`
--
ALTER TABLE `TB_QAL_Questoes_Alternativas_RT`
  ADD CONSTRAINT `TB_QAL_Questoes_Alternativas_RT_ibfk_1` FOREIGN KEY (`QAT_id_questao_atividade`) REFERENCES `TB_QAT_Questoes_Atividades_RT` (`QAT_id_questao_atividade`),
  ADD CONSTRAINT `TB_QAL_Questoes_Alternativas_RT_ibfk_2` FOREIGN KEY (`ALO_id_alternativa_opcao`) REFERENCES `TB_ALO_Alternativas_Opcoes_RT` (`ALO_id_alternativa_opcao`);

--
-- Limitadores para a tabela `TB_QAT_Questoes_Atividades_RT`
--
ALTER TABLE `TB_QAT_Questoes_Atividades_RT`
  ADD CONSTRAINT `TB_QAT_Questoes_Atividades_RT_ibfk_1` FOREIGN KEY (`MOD_id_modelo_3D`) REFERENCES `TB_MOD_Modelos_3D_RT` (`MOD_id_modelo_3D`);

--
-- Limitadores para a tabela `TB_QRT_Questoes_Roteiros_RT`
--
ALTER TABLE `TB_QRT_Questoes_Roteiros_RT`
  ADD CONSTRAINT `TB_QRT_Questoes_Roteiros_RT_ibfk_1` FOREIGN KEY (`QAT_id_questao_atividade`) REFERENCES `TB_QAT_Questoes_Atividades_RT` (`QAT_id_questao_atividade`);

--
-- Limitadores para a tabela `TB_RAU_Ranking_Usuario_RT`
--
ALTER TABLE `TB_RAU_Ranking_Usuario_RT`
  ADD CONSTRAINT `TB_RAU_Ranking_Usuario_RT_ibfk_1` FOREIGN KEY (`USR_id_email_usuario`) REFERENCES `TB_USR_Usuarios_RT` (`USR_id_email_usuario`);

--
-- Limitadores para a tabela `TB_ROA_Roteiros_Atrividades_RT`
--
ALTER TABLE `TB_ROA_Roteiros_Atrividades_RT`
  ADD CONSTRAINT `TB_ROA_Roteiros_Atrividades_RT_ibfk_1` FOREIGN KEY (`USR_id_email_usuario`) REFERENCES `TB_USR_Usuarios_RT` (`USR_id_email_usuario`);

--
-- Limitadores para a tabela `TB_USP_Usuarios_Planos_RT`
--
ALTER TABLE `TB_USP_Usuarios_Planos_RT`
  ADD CONSTRAINT `TB_USP_Usuarios_Planos_RT_ibfk_1` FOREIGN KEY (`USR_id_email_usuario`) REFERENCES `TB_USR_Usuarios_RT` (`USR_id_email_usuario`),
  ADD CONSTRAINT `TB_USP_Usuarios_Planos_RT_ibfk_2` FOREIGN KEY (`PLA_id_plano_assinatura`) REFERENCES `TB_PLA_Planos_Assinatura_RT` (`USR_id_plano_assinatura`);

--
-- Limitadores para a tabela `TB_USR_Usuarios_RT`
--
ALTER TABLE `TB_USR_Usuarios_RT`
  ADD CONSTRAINT `TB_USR_Usuarios_RT_ibfk_1` FOREIGN KEY (`TPU_cod_tipo_usuario`) REFERENCES `TB_TPU_Tipo_Usuario_RT` (`TPU_cod_tipo_usuario`);
