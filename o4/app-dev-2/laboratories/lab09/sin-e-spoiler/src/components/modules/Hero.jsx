const Hero = () => {
  return (
    <article className="hero">
      <div className="container d-flex f-direction-column a-items-center g-4">
        <h1 className="hero__title t-align-center">
          Explore spoiler-free cinema with <span className="c-primary">AI reviews</span>
        </h1>
        <p className="hero__paragraph t-align-center">
          Your movie app with advanced features, premieres, and interactive AR experiences.
        </p>
        <div className="d-flex g-4">
          <a href="#now-showing" className="button button--primary interactive interactive--xl">
            🎬 Browse Movies
          </a>
          <button className="button button--outline-primary interactive interactive--xl">
            🍃 Coming Soon
          </button>
        </div>
      </div>
    </article>
  );
};

export default Hero;