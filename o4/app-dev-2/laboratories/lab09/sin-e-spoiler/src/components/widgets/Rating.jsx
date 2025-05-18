const Rating = ({ value, maxValue = 5 }) => {
  const fullStars = Math.floor(value);
  const hasHalfStar = value % 1 !== 0;
  const emptyStars = maxValue - Math.ceil(value);

  return (
    <div className="rating d-flex a-items-center g-1">
      {[...Array(fullStars)].map((_, i) => (
        <span key={`full-${i}`} className="rating__star">★</span>
      ))}
      {hasHalfStar && <span className="rating__star rating__star--half">★</span>}
      {[...Array(emptyStars)].map((_, i) => (
        <span key={`empty-${i}`} className="rating__star rating__star--empty">☆</span>
      ))}
      <span className="rating__value">{value.toFixed(1)}</span>
    </div>
  );
};

export default Rating;