-- foraneas ruta
ALTER TABLE modelo
    ADD CONSTRAINT fk_marca_modelo
    FOREIGN KEY modelo(marca) 
    REFERENCES marca(clave)
    ON DELETE RESTRICT 
    ON UPDATE CASCADE;

ALTER TABLE ruta
    ADD CONSTRAINT fk_ruta_origen
    FOREIGN KEY ruta(ciudadOrigen) 
    REFERENCES ciudad(codigo)
    ON UPDATE CASCADE ON DELETE RESTRICT;

ALTER TABLE ruta
    ADD CONSTRAINT fk_ruta_destino
    FOREIGN KEY ruta(ciudadDestino) 
    REFERENCES ciudad(codigo)
    ON UPDATE CASCADE ON DELETE RESTRICT;

