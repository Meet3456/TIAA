
import "./planning.css";
import { VerticalTimeline, VerticalTimelineElement } from 'react-vertical-timeline-component';
import {
    StarIcon,

} from "@heroicons/react/24/solid";
import 'react-vertical-timeline-component/style.min.css';
// import timelineElements from './timelineElements'

const planning = () => {
    let timelineElements = [
        {
            id: 1,
            title: "What is retirement planning?",
            "description": "Retirement planning means preparing today for your future life so that you continue to meet all your goals and dreams independently. ",
            buttonText: "Retirement Planning",
        },
        {
            id: 2,
            title: "Why plan for retirement?",
            description:
                "You retire from work, not life. You may have a new set of dreams for your post-retirement life. At the same time, you may also want to maintain your day-to-day lifestyle without worrying about expenses.",
            buttonText: "Plan for retirement",
        },
        {
            id: 3,
            title: "What are advantages of retirement plans",
            description:
                "A retirement plan helps you create a regular flow of income after retirement. Retirement plans offer a fixed income which substitutes for your pre-retirement salary.",
            buttonText: "Advantages of retirement plans",
        },
        {
            id: 5,
            title: "What are importance of retirement plan",
            description:
                "A retirement plan can help you continue your current lifestyle even after retirement. The income from the plan can help you meet your day-to-day expenses and meet your financial goals post retirement.",
            buttonText: "Importance of retirement plan",
        },
        {
            id: 5,
            title: "Where to invest for retirement",
            description:
                "Many investment options can help you save for retirement. Some options may attract higher risks; others may help you protect your wealth.",
            buttonText: "Invest for Retirement",
        },
        {
            id: 6,
            title: "Tips for retirement planning",
            description:
                "Instead of delaying matters for a later stage in life, consider planning for retirement immediately. Saving early gives more time for your money to grow, hence, providing a greater income during your retirement.",
            buttonText: "Tips for Retirement planning",
        },
    ];


    let workIconStyles = { background: "#06D6A0" };
    let schoolIconStyles = { background: "#f9c74f" };
    return (
        <div className="bg-primary-300">
            <h1 className="title text-gray-500">Retirement Planning</h1>
            <VerticalTimeline>
                {timelineElements.map((element, index) => {
                    let isWorkIcon = element.icon === "work";
                    let showButton =
                        element.buttonText !== undefined &&
                        element.buttonText !== null &&
                        element.buttonText !== "";

                    return (
                        <VerticalTimelineElement
                            key={element.id}  // Use index as fallback key
                            date={element.date}
                            dateClassName="date"
                            iconStyle={isWorkIcon ? workIconStyles : schoolIconStyles}
                            icon={isWorkIcon ? <StarIcon /> : <StarIcon />}
                        >
                            <h3 className="vertical-timeline-element-title ">
                                {element.title}
                            </h3>
                            <h5 className="vertical-timeline-element-subtitle">
                                {element.location}
                            </h5>
                            <p id="description">{element.description}</p>
                            {showButton && (
                                <a
                                    className={`button bg-[#0ac593]`}
                                    href="/"
                                >
                                    {element.buttonText}
                                </a>
                            )}
                        </VerticalTimelineElement>
                    );
                })}
            </VerticalTimeline>
        </div>
    )
}

export default planning