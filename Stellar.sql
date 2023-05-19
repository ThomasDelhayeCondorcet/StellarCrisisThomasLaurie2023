-- General Parameters
CREATE TABLE param ( -- Singleton
    loginmsg    TEXT
);

-- Définition des séries
CREATE TABLE series(
    sid                 SERIAL PRIMARY KEY,
    sname               VARCHAR(20), -- Nom de la série
    descr               VARCHAR(64), -- Description courte
    fulldesc            TEXT,     -- Description longue
    color               VARCHAR(7),  -- Couleur de la série (#rrggbb) (server_color)
    simage              VARCHAR(64),  -- Fichier image par défaut pour la série (empty.gif)
    count               INTEGER DEFAULT 0,  -- Nombre de parties en cours dans la série
    gcnt                INTEGER DEFAULT 0,  -- Numéro de la dernière partie créée
    spawnfirst          INTEGER,  -- Spawn new when 1st player joined (No)
    max                 FLOAT,    -- Max games simultanés (10)
    wins                INTEGER,  -- Nombre de victoires minimum pour rejoindre (1)
    winmax              INTEGER,  -- Nome de victoires maximum pour rejoinre (-1)
    bridier             INTEGER,  -- Bridier Ranking (No)

    utime               INTEGER,  -- Temps entre updates (24h)
    timelimit           INTEGER,  -- Temps avant overtime (24h)
    overtime            INTEGER,  -- Temps entre update après la limite (24h)
    weekend             INTEGER,  -- 1 = Updates pendant le week-end (1)
    fromhr              INTEGER,  -- heure début mises à jour (0)            | De 0:00 à 23/59
    tohr                INTEGER,  -- heure fin mises à jour (incluse) (23)   |
    udelay              INTEGER,  -- delay avant 1ere mise à jour (24h)

    availrestrict       INTEGER,  -- Tech restreintes autorisées  (0)
    tradeinrestrict     INTEGER,  -- Trade In tech restreintes (0)
    inittech            FLOAT,    -- Niveau technologique initial (1)
    tmult               FLOAT,    -- Tech multiplier (1.5)

    initcloak           INTEGER,  -- Cloak on build (No)
    maxship             FLOAT,    -- Max vaisseaux par joueur (0 = unlimited)
    stargate            FLOAT,    -- Multiplicateur portée stargate (0 = unlimited)
    jumpgate            FLOAT,    -- Multiplicateur portée jumpgate (1)
    engloss             FLOAT,    -- Perte BR Engineer (0.5)
    jumploss            FLOAT,    -- Perte BR jumpgate (0.5)
    morphloss           FLOAT,    -- Perte BR morpher (0.5)
    carloss             FLOAT,    -- Perte BR Carrier (0.5)
    morpherbuild        INTEGER,  -- Coût extra construction morpher (75)
    morphermaint        INTEGER,  -- Coût extra maintenance morpher (12)
    builderbuild        INTEGER,  -- Coût construction builder (75)
    buildermaint        INTEGER,  -- Coût maintenance builder (16)
    jumpgatebuild       INTEGER,  -- Coût construction jumpgate (100)
    jumpgatemaint       INTEGER,  -- Coût maintenance jumpgate (24)
    carrierbuild        INTEGER,  -- Coût construction carrier (100)
    carriermaint        INTEGER,  -- Coût maintenance carrier (16)
    plabuild            INTEGER,  -- Minimum to build planet (90)

    avgag               INTEGER,  -- Minimum average Ag (30)
    avgmin              INTEGER,  -- Minimum average Minerals (30)
    avgfuel             INTEGER,  -- Minimum average fuel (30)
    rangeag             INTEGER,  -- Range Ag (0)
    rangemin            INTEGER,  -- Range Min (0)
    rangefuel           INTEGER,  -- Range Fuel (0)
    homeag              INTEGER,  -- Ag HomeWorld (100)
    homemin             INTEGER,  -- Min HomeWorld (100)
    homefuel            INTEGER,  -- Fuel HomeWorld (100)
    maxag               INTEGER,  -- Agriculture ratio max (100)
    minbuild            INTEGER,  -- Population Minimale pour construire (50)
    smin                INTEGER,  -- Nombre minimum de systèmes (8)
    smax                INTEGER,  -- Nombre maximum de systèmes (10)
    layout              INTEGER,   -- 1 = Traditionnel, 2 = Mirror (1)

    pmax                INTEGER,  -- Nombre max de joueurs dans une partie (6)
    maxallies           INTEGER,  -- Nombre maximum d'alliés (1)
    blood               INTEGER,  -- 0 alliances, 1 pas d'alliances, 2 trade/truce (0)
    surrdraw            INTEGER,  -- Allow Surrender (1)
    blind               INTEGER,  -- Blind avant début de partie (0)
    vis                 INTEGER,  -- build visibility (No)
    visp                INTEGER  -- Player visibility in gamelist (No)
);

-- Instance d'une Série (tables accessoires seront créées : planètes, joueurs, vaisseaux, flottes, diplomatie, exploration)

CREATE TABLE game (
    gid                 SERIAL PRIMARY KEY,
    sid                 INTEGER REFERENCES series(sid) ON DELETE CASCADE ON UPDATE CASCADE,
    gnumber             INTEGER,  -- Numéro de partie dans la série
    fullgame            INTEGER DEFAULT 0,  -- Nombre de joueurs ayant rejoint
    ufirst              INTEGER,  -- TS 1er update
    ulast               INTEGER,  -- TS dernier update fait
    utime               INTEGER,  -- Délai entre updates
    ucnt                INTEGER DEFAULT 0, -- Numéro d'update
    sadd                INTEGER,  -- Nombre de systèmes par joueur
    avgag               INTEGER,  -- Ag Moyen
    avgmin              INTEGER,  -- Minerai moyen
    avgfuel             INTEGER,  -- Fuel moyen
    bridier             INTEGER,  -- Bridier actif ?
    numplanets          INTEGER DEFAULT 0,  -- Nombre de planètes existantes
    history             TEXT      -- Historique partie.
);

-- Utilisateur

CREATE TABLE player (
    pid                 SERIAL PRIMARY KEY,
    uname               VARCHAR(20), -- Username
    passwd              VARCHAR(64), -- Mot de passe
    realname            VARCHAR(64), -- Nom Réel
    email               VARCHAR(64), -- E-Mail
    showemail           INTEGER,     -- Show E-Mail ?
    alien               INTEGER,     -- Numéro d'Alien
    bridiertime         INTEGER DEFAULT 0, -- TS dernier ajustement Bridier
    bridieridx          INTEGER DEFAULT 0, -- Index Bridier
    bridierrank         INTEGER DEFAULT 0, -- Rang Bridier
    wins                INTEGER DEFAULT 0, -- Nombre victoires
    kills               INTEGER DEFAULT 0, -- Nombre kills (HW nuke)
    ruined              INTEGER DEFAULT 0, -- Nombre chute en ruine (idle)
    killed              INTEGER DEFAULT 0, -- Nombre de fois tués (HW Nuke)
    maxepow             INTEGER DEFAULT 0, -- Max Economic Power
    maxmpow             INTEGER DEFAULT 0, -- Max Military Power
    missive             TEXT DEFAULT '',   -- Missive (flash messages)
    lastlog             INTEGER DEFAULT 0, -- TS dernière connexion
    lastip              VARCHAR(32),       -- Dernière IP
    bcast               TEXT DEFAULT '',   -- Messages Broadcastés
    bgimage             INTEGER,     -- Afficher image de fond
    eratio              INTEGER,     -- Enhanced Ratios
    nextbr              INTEGER,     -- Display Next BR
    sort1               INTEGER,     -- 1er critère de tri
    sort2               INTEGER,     -- 2eme critère de tri
    sort3               INTEGER,     -- 3eme critère de tri
    cmt                 TEXT,        -- Commentaire compte
    victory             TEXT         -- "Victory Sneer"
);

-- Liste des technologies. Attention, la gestion côté programme demandera des noms exacts

CREATE TABLE tech (
    tid                 SERIAL PRIMARY KEY,
    vaisseau            VARCHAR(20),
    canmove             INTEGER
);

INSERT INTO tech(vaisseau,canmove)
    VALUES('Attack',1),
          ('Science',1),
          ('Colony',1),
          ('Stargate',0),
          ('Cloaker',1),
          ('Satellite',0),
          ('Terraformer',1),
          ('Troopship',1),
          ('Doomsday',1),
          ('Minefield',0),
          ('Minesweeper',1),
          ('Engineer',1),
          ('Builder',1),
          ('Morpher',1),
          ('Carrier',1),
          ('Jumpgate',0);

-- Technologies acceptées/restreintes/développées dans une série

CREATE TABLE serietech(
    sid     INTEGER REFERENCES series(sid) ON DELETE CASCADE ON UPDATE CASCADE,
    tid     INTEGER REFERENCES tech(tid) ON DELETE CASCADE ON UPDATE CASCADE,
    allowed INTEGER -- 0 Not Allowed, 1 Restricted, 2 Available, 3 developped
);

-- Paramètre des joueurs dans des parties

CREATE TABLE usergame(
    pgid            SERIAL PRIMARY KEY,
    pid             INTEGER REFERENCES player(pid) ON DELETE CASCADE ON UPDATE CASCADE,
    gid             INTEGER REFERENCES game(gid) ON DELETE CASCADE ON UPDATE CASCADE,
    build           INTEGER, -- Build cost for this turn
    maint           INTEGER, -- Maintenance cost for this turn
    fuse            INTEGER, -- Fuel used for this turn
    mineral         INTEGER, -- Total minerals produced
    fuel            INTEGER, -- Total fuel produced
    ag              INTEGER, -- Total Ag produced
    pop             INTEGER, -- Current population
    maxpop          INTEGER, -- Target population
    epow            INTEGER, -- Economic Power
    mpow            INTEGER, -- Military Power
    minr            FLOAT,   -- Mineral Ratio
    fuelr           FLOAT,   -- Fuel Ratio
    agr             FLOAT,   -- Agriculture ratio
    techd           FLOAT,   -- Tech Development
    lastax          INTEGER, -- TS dernier accès
    lastupd         INTEGER, -- Last Update
    lastip          VARCHAR(32), -- Last IP address
    endturn         INTEGER  -- Ready for next turn
);

-- Planètes présentes dans une partie

CREATE TABLE systemgame (
    sid       SERIAL PRIMARY KEY,
    gid       INTEGER REFERENCES game (gid) ON DELETE CASCADE ON UPDATE CASCADE,
    sname     VARCHAR(20),
    mineral   INTEGER,
    fuel      INTEGER,
    ag        INTEGER,
    pop       INTEGER DEFAULT 0,
    vispop    INTEGER DEFAULT 0,
    popvis    INTEGER DEFAULT 0,
    maxpopvis INTEGER DEFAULT 0,
    own       INTEGER DEFAULT NULL REFERENCES player (pid) ON DELETE SET NULL ON UPDATE CASCADE,
    home      INTEGER DEFAULT NULL REFERENCES player (pid) ON DELETE SET NULL ON UPDATE CASCADE
);

-- Liens entre planètes dans une partie

CREATE TABLE systemlink (
    slid      SERIAL PRIMARY KEY,
    sfrom     INTEGER REFERENCES systemgame(sid) ON DELETE CASCADE ON UPDATE CASCADE,
    sto       INTEGER REFERENCES systemgame(sid) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Planetes explorées par un joueur dans une partie

CREATE TABLE systemexp (
    seid        SERIAL PRIMARY KEY,
    sid         INTEGER REFERENCES systemgame(sid) ON DELETE CASCADE ON UPDATE CASCADE,
    pgid         INTEGER REFERENCES usergame(pgid) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Relations diplomatiques entre joueurs dans une partie

CREATE TABLE playerdip (
    pdid        SERIAL PRIMARY KEY,
    pgid        INTEGER REFERENCES usergame(pgid) ON DELETE CASCADE ON UPDATE CASCADE,
    topgid      INTEGER REFERENCES usergame(pgid) ON DELETE CASCADE ON UPDATE CASCADE,
    dip         INTEGER DEFAULT 2,
    dipoffer    INTEGER DEFAULT 2
);

-- Vaisseaux

CREATE TABLE shipgame (
    sgid        SERIAL PRIMARY KEY,
    pgid        INTEGER REFERENCES usergame(pgid) ON DELETE CASCADE ON UPDATE CASCADE,
    maxbr       FLOAT,
    br          FLOAT,
    fuel        INTEGER,
    maint       INTEGER,
    shiptype    INTEGER REFERENCES tech(tid),
    nextorder   INTEGER,
    nextdest    INTEGER REFERENCES systemgame(sid) ON DELETE CASCADE ON UPDATE CASCADE,
    nextdata    VARCHAR(20)
);
