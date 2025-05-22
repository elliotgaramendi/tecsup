const Footer = () => {
  const currentYear = new Date().getFullYear();

  return (
    <footer className="footer">
      <nav className="nav">
        <div className="container g-layout g-layout--auto-fit-columns g-10">
          <div className="d-flex f-direction-column g-2">
            <a href="#"><img src="/logo.svg" alt="Sin E Spoiler Logo" className="img img--logo" /></a>
            <h2 className="interactive interactive--lg c-primary">Sin E Spoiler</h2>
            <p className="text text--xs c-secondary-text">
              Your trusted source for spoiler-free movie experiences. AI-powered reviews that preserve the magic of cinema.
            </p>
          </div>
          <div className="d-flex f-direction-column g-2">
            <h3 className="interactive interactive--lg">Showtimes</h3>
            <ul className="list d-flex f-direction-column g-1">
              <li><a href="#now-showing" className="link interactive interactive--sm c-secondary-text">Now Showing</a></li>
              <li><a href="#coming-soon" className="link interactive interactive--sm c-secondary-text">Coming Soon</a></li>
              <li><a href="#premieres" className="link interactive interactive--sm c-secondary-text">Premiere Giveaways</a></li>
            </ul>
          </div>
          <div className="d-flex f-direction-column g-2">
            <h3 className="interactive interactive--lg">Explore</h3>
            <ul className="list d-flex f-direction-column g-1">
              <li><a href="#faq" className="link interactive interactive--sm c-secondary-text">FAQs</a></li>
              <li><a href="#about" className="link interactive interactive--sm c-secondary-text">About Us</a></li>
              <li><a href="#blog" className="link interactive interactive--sm c-secondary-text">Cinema Blog</a></li>
            </ul>
          </div>
          <div className="d-flex f-direction-column g-2">
            <h3 className="interactive interactive--lg">Social Media</h3>
            <ul className="list d-flex f-direction-column g-1">
              <li><a href="https://www.instagram.com/elliotgaramendi/" className="link interactive interactive--sm c-secondary-text">Instagram</a></li>
              <li><a href="https://x.com/elliotgaramendi" className="link interactive interactive--sm c-secondary-text">X</a></li>
              <li><a href="https://www.youtube.com/@elliotgaramendi" className="link interactive interactive--sm c-secondary-text">YouTube</a></li>
            </ul>
          </div>
        </div>
      </nav>
      <nav className="nav">
        <div className="container flexbox flexbox--centered-spacing flexbox--responsive g-2">
          <h2 className="interactive interactive--xs">
            <a href="https://www.instagram.com/elliotgaramendi/" className="link interactive interactive--xs">
              Elliot Garamendi</a> &copy; {currentYear} <a href="https://www.linkedin.com/in/elliotgaramendi/" className="link interactive interactive--xs">
              Sin E Spoiler.
            </a>
            All rights reserved.
          </h2>
          <h2 className="interactive interactive--xs">
            Made with ♥️ by: <a href="https://www.instagram.com/elliotgaramendi/" className="link interactive interactive--xs">
              Elliot Garamendi
            </a>
          </h2>
        </div>
      </nav>
    </footer>
  );
};

export default Footer;