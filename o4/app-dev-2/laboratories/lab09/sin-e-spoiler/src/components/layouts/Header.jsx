const Header = () => {
  return (
    <header className="header">
      <nav className="nav nav--scroll">
        <div className="container d-flex a-items-center j-content-between g-4">
          <a href="#" className="d-flex a-items-center g-2">
            <img src="/logo.svg" alt="Sin E Spoiler" width="32" height="32" />
            <strong className="c-primary">Sin E Spoiler</strong>
          </a>
          <ul className="list d-flex g-5 f-2 j-content-center">
            <li><a href="#movies" className="link interactive">Movies</a></li>
            <li><a href="#cinemas" className="link interactive">Cinemas</a></li>
            <li><a href="#promotions" className="link interactive">Promotions</a></li>
            <li><a href="#tickets" className="link interactive">My Tickets</a></li>
            <li><a href="#ar" className="link interactive">AR Posters</a></li>
          </ul>
          <div className="d-flex g-3">
            <a href="#signin" className="button button--primary interactive">🎟️ Sign In</a>
          </div>
        </div>
      </nav>
    </header>
  );
};

export default Header;