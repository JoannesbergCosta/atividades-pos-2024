import { getArtistas, createArtista, getAlbuns, createAlbum, getMusicas, createMusica } from "./api";

document.addEventListener("DOMContentLoaded", async () => {
  const artistasList = document.getElementById("artistas");
  const albunsList = document.getElementById("albuns");
  const musicasList = document.getElementById("musicas");

  const artistas = await getArtistas();
  artistasList.innerHTML = artistas.map(artista => `<li>${artista.nome} (${artista.local})</li>`).join("");

  const albuns = await getAlbuns();
  albunsList.innerHTML = albuns.map(album => `<li>${album.nome} (${album.ano})</li>`).join("");

  const musicas = await getMusicas();
  musicasList.innerHTML = musicas.map(musica => `<li>${musica.nome} (${musica.segundos}s)</li>`).join("");

  const artistaForm = document.getElementById("artista-form");
  artistaForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    const formData = new FormData(artistaForm);
    const artista = {
      nome: formData.get("nome"),
      local: formData.get("local"),
      ano_criacao: formData.get("ano_criacao"),
    };
    await createArtista(artista);
    window.location.reload();
  });
});
