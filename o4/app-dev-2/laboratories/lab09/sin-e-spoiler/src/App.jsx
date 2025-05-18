import Footer from "./components/layouts/Footer";
import Header from "./components/layouts/Header";
import Hero from "./components/modules/Hero";
import MovieList from "./components/modules/MovieList";
import { getMovies } from "./utils/movie.utils";

function App() {
  const movies = getMovies();

  return (
    <>
      <Header />
      <main className="main">
        <Hero />
        <MovieList movies={movies} />
      </main>
      <Footer />
    </>
  );
}

export default App;
