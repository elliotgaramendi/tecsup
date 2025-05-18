import MovieCard from "../components/MovieCard";

const MovieList = ({ movies }) => {
  return (
    <section id="movies" className="section">
      <div className="container d-flex f-direction-column g-8">
        <h2 className="title c-primary t-align-center">Now Showing</h2>
        <div className="g-layout g-layout--auto-fit-columns g-8">
          {movies.map(movie => (
            <MovieCard key={movie.id} movie={movie} />
          ))}
        </div>
      </div>
    </section>
  );
};

export default MovieList;