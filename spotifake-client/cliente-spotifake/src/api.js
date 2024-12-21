const API_URL = "http://127.0.0.1:8000/";

export const getArtistas = async () => {
  const response = await fetch(`${API_URL}artistas/`);
  return response.json();
};

export const createArtista = async (artista) => {
  const response = await fetch(`${API_URL}artistas/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(artista),
  });
  return response.json();
};

export const getAlbuns = async () => {
  const response = await fetch(`${API_URL}albuns/`);
  return response.json();
};

export const createAlbum = async (album) => {
  const response = await fetch(`${API_URL}albuns/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(album),
  });
  return response.json();
};

export const getMusicas = async () => {
  const response = await fetch(`${API_URL}musicas/`);
  return response.json();
};

export const createMusica = async (musica) => {
  const response = await fetch(`${API_URL}musicas/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(musica),
  });
  return response.json();
};
