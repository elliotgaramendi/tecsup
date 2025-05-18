import { tmdbNowPlayingMock } from "../data/movies.data";

export const getImageUrl = (size = "w342", path) => {
  if (!path) return "https://picsum.photos/342/513?random";
  return `https://image.tmdb.org/t/p/${size}${path}`;
};

export const genres = {
  12: "Adventure",
  14: "Fantasy",
  28: "Action",
  35: "Comedy",
  53: "Thriller",
  80: "Crime",
  878: "Sci-Fi",
  10751: "Family",
  10752: "War",
  18: "Drama",
  9648: "Mystery",
  27: "Horror",
  10749: "Romance",
  37: "Western"
};

export const mapTmdbToMovie = (tmdbMovie) => {
  return {
    id: tmdbMovie.id,
    title: tmdbMovie.title,
    rating: Math.round(tmdbMovie.vote_average) / 2,
    genre: tmdbMovie.genre_ids.map(id => genres[id] || "Drama")[0],
    duration: "120 min",
    image: getImageUrl("w342", tmdbMovie.poster_path),
    description: tmdbMovie.overview,
    showTimes: ["2:30 PM", "5:45 PM", "9:00 PM", "11:30 PM"],
    releaseDate: tmdbMovie.release_date
  };
};

export const getMovies = () => tmdbNowPlayingMock.results.map(mapTmdbToMovie);