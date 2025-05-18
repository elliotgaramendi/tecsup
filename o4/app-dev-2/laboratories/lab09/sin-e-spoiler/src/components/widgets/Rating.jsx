const Rating = ({ value, maxValue = 5 }) => {
  const fullStars = Math.floor(value);
  const hasHalfStar = value % 1 !== 0;
  const emptyStars = maxValue - Math.ceil(value);

  return (
    <div className="d-flex a-items-center g-2">
      <div className="d-flex a-items-center g-1">
        {[...Array(fullStars)].map((_, i) => (
          <span key={`full-${i}`} className="interactive interactive--lg c-warning">★</span>
        ))}
        {hasHalfStar && <span className="interactive interactive--lg">★</span>}
        {[...Array(emptyStars)].map((_, i) => (
          <span key={`empty-${i}`} className="interactive interactive--lg">☆</span>
        ))}
      </div>
      <span className="interactive">{value.toFixed(1)}</span>
    </div>
  );
};

export default Rating;