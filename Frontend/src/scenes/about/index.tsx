import { SelectedPage, ClassType } from "../../shared/types";
import image1 from "../../assets/image1.jpeg";
import image2 from "../../assets/image2.jpeg";
import image3 from "../../assets/image3.jpeg";
import image4 from "../../assets/image4.jpeg";
import image5 from "../../assets/image5.jpeg";
import image6 from "../../assets/image6.jpeg";
import { motion } from "framer-motion";
import HText from "../../shared/Htext";
import Class from "./Class";

const classes: Array<ClassType> = [
  {
    name: "Retirement Planning",
    description:
      "Gather client data for personalized retirement goals.Utilize AI for risk assessment and customized portfolios based on market trends, ensuring tailored financial plans.",
    image: image1,
  },
  {
    name: "StartUp Ideas",
    description:"AI-driven ideation links work experiences with personal interests, creating unique business opportunities aligned with individual skills and passions.",
    image: image2,
  },
  {
    name: "Social Engagement Community",
    description:
      "Combat loneliness through local events, online communities, and cultural activities, fostering vibrant connections and a socially engaged lifestyle.",
    image: image3,
  },
  {
    name: "Initial User Interaction",
    description:
      "Engage users in financial conversations to understand goals and risk attitudes.",
    image: image4,
  },
  {
    name: "Healthcare and Longevity Predictions",
    description : "AI-driven health analytics predict life expectancy and healthcare costs for informed long-term financial planning.",
    image: image5,
  },
  {
    name: "Investment Suggestions",
    description:
      "Leverage assessed risk tolerance for personalized investment suggestions.",
    image: image6,
  },
];

type Props = {
  setSelectedPage: (value: SelectedPage) => void;
};

const About = ({ setSelectedPage }: Props) => {
  return (
    <section id="aboutus" className="w-full bg-primary-100 py-40">
      <motion.div
        onViewportEnter={() => setSelectedPage(SelectedPage.OurClasses)}
      >
        <motion.div
          className="mx-auto w-5/6"
          initial="hidden"
          whileInView="visible"
          viewport={{ once: true, amount: 0.5 }}
          transition={{ duration: 0.5 }}
          variants={{
            hidden: { opacity: 0, x: -50 },
            visible: { opacity: 1, x: 0 },
          }}
        >
          <div className="md:w-3/5">
            <HText>About Us</HText>
            <p className="py-5">

              Empowering futures through innovative solutions with a commitment to excellence, we leverage cutting-edge technology to deliver personalized and secure product that cater to the unique needs of our clients. 
            </p>
          </div>
        </motion.div>
        <div className="mt-10 h-[353px] w-full overflow-x-auto overflow-y-hidden">
          <ul className="w-[2800px] whitespace-nowrap">
            {classes.map((item: ClassType, index) => (
              <Class
                key={`${item.name}-${index}`}
                name={item.name}
                description={item.description}
                image={item.image}
              />
            ))}
          </ul>
        </div>
      </motion.div>
    </section>
  );
};

export default About;