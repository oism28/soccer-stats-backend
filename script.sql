CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(120) NOT NULL UNIQUE,
    contrasena VARCHAR(128) NOT NULL
);

CREATE TABLE equipos_favoritos (
    equipo_id INTEGER NOT NULL,
    usuario_id INTEGER NOT NULL,
    PRIMARY KEY (equipo_id, usuario_id),
    CONSTRAINT fk_equipos_usuario FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    CONSTRAINT uq_equipo_usuario UNIQUE (equipo_id, usuario_id)
);

CREATE TABLE competiciones_favoritas (
    competicion_id INTEGER NOT NULL,
    usuario_id INTEGER NOT NULL,
    PRIMARY KEY (competicion_id, usuario_id),
    CONSTRAINT fk_competicion_usuario FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    CONSTRAINT uq_competicion_usuario UNIQUE (competicion_id, usuario_id)
);

CREATE TABLE jugadores_favoritos (
    jugador_id INTEGER NOT NULL,
    usuario_id INTEGER NOT NULL,
    PRIMARY KEY (jugador_id, usuario_id),
    CONSTRAINT fk_jugador_usuario FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    CONSTRAINT uq_jugador_usuario UNIQUE (jugador_id, usuario_id)
);
