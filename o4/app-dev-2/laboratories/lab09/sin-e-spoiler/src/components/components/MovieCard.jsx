import Rating from "../widgets/Rating";

const MovieCard = ({ movie }) => {
  const { title, rating, genre, duration, image, description, showTimes } = movie;

  return (
    <article className="card card--movie">
      <div className="card__header">
        <img
          src={image}
          alt={`${title} poster`}
          className="card__image"
          loading="lazy"
        />
        <div className="card__overlay">
          <span className="badge badge--primary">{genre}</span>
        </div>
      </div>

      <div className="card__body">
        <h3 className="card__title">{title}</h3>
        <div className="card__meta d-flex g-2">
          <Rating value={rating} />
          <span className="card__duration">{duration}</span>
        </div>

        <p className="card__description">{description}</p>

        <div className="card__showtimes">
          <h4 className="card__subtitle">Today's Showtimes</h4>
          <div className="d-flex f-wrap g-2">
            {showTimes.map((time, index) => (
              <button
                key={index}
                className="button button--time"
                aria-label={`Show time ${time} for ${title}`}
              >
                {time}
              </button>
            ))}
          </div>
        </div>
      </div>
    </article>
  );
};

export default MovieCard;