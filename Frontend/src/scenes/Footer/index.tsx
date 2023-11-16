import Logo from "../../assets/logo_new.png";

const Footer = () => {
  return (
    <footer className="bg-primary-100 py-16">
      <div className="justify-content mx-auto w-5/6 gap-16 md:flex">
        <div className="mt-16 basis-1/2 md:mt-0">
          <img alt="logo" src={Logo} className="w-[50%]"/>
          <p className="my-5">
          Empowering futures through innovative solutions with a commitment to excellence, we leverage cutting-edge technology to deliver personalized and secure product that cater to the unique needs of our clients.
          </p>
          <p>© EasyRetireAi All Rights Reserved.</p>
        </div>
        <div className="mt-16 basis-1/4 md:mt-0">
          <h4 className="font-bold">Links</h4>
          <p className="my-5">LinkedIn</p>
          <p className="my-5">Instagram</p>
        </div>
        <div className="mt-16 basis-1/4 md:mt-0">
          <h4 className="font-bold">Contact Us</h4>
          <p className="my-5"></p>
          <p>(333)425-6825</p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;