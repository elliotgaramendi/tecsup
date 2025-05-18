const Footer = () => {
  const currentYear = new Date().getFullYear();

  return (
    <footer className="footer">
      <div className="container g-layout g-layout--auto-fit-columns g-5">
        <div className="d-flex f-direction-column g-2">
          <a href="#"><img src="/logo.svg" alt="Sin E Spoiler Logo" className="img img--logo" /></a>
          <h2 className="interactive interactive--lg">Sin E Spoiler</h2>
          <p className="text text--xs">Enjoy spoiler-free cinema, smart reviews, and exclusive experiences.</p>
        </div>
        <div className="d-flex f-direction-column g-2">
          <h3 className="interactive interactive--lg">Showtimes</h3>
          <ul className="list d-flex f-direction-column g-1">
            <li><a href="#now-showing" className="link interactive interactive--sm">Now Showing</a></li>
            <li><a href="#coming-soon" className="link interactive interactive--sm">Coming Soon</a></li>
            <li><a href="#premieres" className="link interactive interactive--sm">Premiere Giveaways</a></li>
          </ul>
        </div>
        <div className="d-flex f-direction-column g-2">
          <h3 className="interactive interactive--lg">Explore</h3>
          <ul className="list d-flex f-direction-column g-1">
            <li><a href="#faq" className="link interactive interactive--sm">FAQs</a></li>
            <li><a href="#about" className="link interactive interactive--sm">About Us</a></li>
            <li><a href="#blog" className="link interactive interactive--sm">Cinema Blog</a></li>
          </ul>
        </div>
        <div className="d-flex f-direction-column g-2">
          <h3 className="interactive interactive--lg">Social Media</h3>
          <ul className="list d-flex f-direction-column g-1">
            <li><a href="#" className="link interactive interactive--sm">Instagram</a></li>
            <li><a href="#" className="link interactive interactive--sm">YouTube</a></li>
            <li><a href="#" className="link interactive interactive--sm">TikTok</a></li>
          </ul>
        </div>
      </div>
      <nav className="nav">
        <div className="container flexbox flexbox--centered-spacing flexbox--responsive g-2">
          <p className="interactive interactive--xs">&copy; {currentYear} Sin E Spoiler. All rights reserved.</p>
          <p className="interactive interactive--xs">Developed by <a href="https://www.instagram.com/elliotgaramendi/" className="link interactive interactive--xs">Elliot Garamendi</a></p>
        </div>
      </nav>
    </footer>
  );
};

export default Footer;