CREATE DATABASE IF NOT EXISTS `nsi_eleve6`;
USE `nsi_eleve6`;

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

--
-- Base de données : `nsi_eleve6`
--

-- --------------------------------------------------------

--
-- Structure de la table `utilisateurs`
--

CREATE TABLE `utilisateurs` (
  `id` int(11) NOT NULL,
  `nom` mediumtext DEFAULT NULL,
  `prenom` mediumtext DEFAULT NULL,
  `pseudonyme` mediumtext DEFAULT NULL,
  `mot_de_passe` mediumtext DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `utilisateurs`
--

INSERT INTO `utilisateurs` (`id`, `nom`, `prenom`, `pseudonyme`, `mot_de_passe`) VALUES
(1, 'R', 'R', 'Ruben', 'aze'),
(2, 'Y', 'Y', 'Yuna', 'aze');

--
-- Structure de la table `chat`
--

-- --------------------------------------------------------


CREATE TABLE `chat` (
  `id` int(11) NOT NULL,
  `id_eleve` int(11) DEFAULT NULL,
  `message` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `chat`
--

INSERT INTO `chat` (`id`, `id_eleve`, `message`) VALUES
(1, 1, 'Bonjour'),
(2, 2, 'Salut, ça va ?'),
(3, 1, 'ça va et toi ?');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `chat`
--
ALTER TABLE `chat`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `utilisateurs`
--
ALTER TABLE `utilisateurs`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `chat`
--
ALTER TABLE `chat`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT pour la table `utilisateurs`
--
ALTER TABLE `utilisateurs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;
