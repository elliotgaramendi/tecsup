const Header = () => {
  return (
    <header className="header">
      <nav className="nav nav--scroll">
        <div className="container d-flex a-items-center g-4">
          <a href="#" className="link f-1 d-flex a-items-center g-2">
            <img src="/logo.svg" alt="Sin E Spoiler" width="32" height="32" />
            <h2 className="interactive interactive--lg c-primary">Sin E Spoiler</h2>
          </a>
          <div className="off-canvas off-canvas--right off-canvas--mobile" id="menu">
            <a
              href="#"
              className="off-canvas__backdrop"
            ></a>
            <div className="off-canvas__child">
              <ul className="list f-2 list flexbox flexbox--center flexbox--responsive g-8">
                <li><a href="#movies" className="link interactive">Movies</a></li>
                <li><a href="#cinemas" className="link interactive">Cinemas</a></li>
                <li><a href="#promotions" className="link interactive">Promotions</a></li>
                <li><a href="#tickets" className="link interactive">My Tickets</a></li>
                <li><a href="#ar" className="link interactive">AR Posters</a></li>
              </ul>
            </div>
          </div>
          <div className="f-1 d-flex a-items-center j-content-end g-2">
            <a href="#signin" className="button button--primary interactive">💕 Sign In</a>
            <a href="#menu" className="link interactive interactive--2xl md:d-none">
              📚
            </a>
          </div>
        </div>
      </nav>
    </header>
  );
};

export default Header;