import user from '../../assets/user1.jpeg'
import user2 from '../../assets/user2.jpeg'
import user3 from '../../assets/user3.jpeg'
import workoutImage from '../../assets/workoutImage.jpeg'
import yogaPose from '../../assets/yogapose.jpeg'
import watercolorArt from '../../assets/watercolorArt.jpg'
import abstractArt from '../../assets/abstractArt.jpeg'
import volunteerImage1 from '../../assets/volunteerImage1.jpeg'
import volunteerImage4 from '../../assets/volunteerImage4.jpeg'
import chefImage from '../../assets/chefImage.jpeg'
import cookieImage from '../../assets/cookieImage.jpeg'
import cyclistImage from '../../assets/cyclistImage.jpeg'
import mountainBikingImage from '../../assets/mountainBikingImage.jpeg'
import logo from '../../assets/logo_new.png'
import Card from '../card'
import { useState } from 'react'
import { NavLink } from 'react-router-dom'
const community = () => {
  const [exercise, setExercise] = useState(true);
  const [painting, setPainting] = useState(false);
  const [cycling, setCycling] = useState(false);
  const [cooking, setCooking] = useState(false);
  const [volunteer, setVolunteer] = useState(false);

  const Exercise = () => {
    // Update the state when the button is clicked
    setExercise(true);
    setCooking(false);
    setPainting(false);
    setCycling(false);
    setVolunteer(false);

  };
  const Painting = () => {
    // Update the state when the button is clicked
    setExercise(false);
    setCooking(false);
    setPainting(true);
    setCycling(false);
    setVolunteer(false);

  };
  const Cycling = () => {
    // Update the state when the button is clicked
    setExercise(false);
    setCooking(false);
    setPainting(false);
    setCycling(true);
    setVolunteer(false);

  };
  const Cooking = () => {
    // Update the state when the button is clicked
    setExercise(false);
    setCooking(true);
    setPainting(false);
    setCycling(false);
    setVolunteer(false);

  };
  const Volunteer = () => {
    // Update the state when the button is clicked
    setExercise(false);
    setCooking(false);
    setPainting(false);
    setCycling(false);
    setVolunteer(true);

  };
  const cyclingCardData = [
    {
      time: "Fri 10:15, 6 hours ago",
      user: "Cycling Enthusiast",
      message: "Just finished an exhilarating 20-mile ride through scenic mountain trails. The fresh air and breathtaking views make every pedal stroke worthwhile!",
      image: cyclistImage,
    },
    {
      time: "Thu 15:45, 1 day ago",
      user: "Bike Commuter",
      message: "Commuted to work on my bike again today. It's not just a commute; it's a mini adventure! Plus, it's an eco-friendly way to start the day.",
    },
    {
      time: "Wed 20:30, 2 days ago",
      user: "Mountain Biker",
      message: "Explored some challenging mountain trails today. The rush of adrenaline going downhill is unmatched! 🚵‍♂️ #MountainBiking #Adventure",
      image: mountainBikingImage,
    },
    {
      time: "Tue 12:00, 3 days ago",
      user: "Cycling Community",
      message: "Joining a cycling group has been the best decision! Today's group ride was a blast. It's amazing how cycling brings people together. 🚴‍♀️🚴‍♂️ #CyclingCommunity",
    },
  ];


  const cookingCardData = [
    {
      time: "Fri 6:15 PM",
      user: "Chef Julia",
      message: "Just tried a new recipe for garlic butter shrimp. It's incredibly flavorful and quick to make! Here's the recipe:\n- Saute shrimp in garlic butter\n- Add a pinch of paprika and salt\n- Squeeze fresh lemon juice before serving",
      image: chefImage,
    },
    {
      time: "Thu 10:45 AM",
      user: "Foodie Explorer",
      message: "Exploring street food in Thailand! Just had the most amazing Pad Thai from a local vendor. The combination of sweet, sour, and spicy flavors is mind-blowing.",
    },
    {
      time: "Wed 3:30 PM",
      user: "Baking Enthusiast",
      message: "Baked a batch of chocolate chip cookies today! Used a mix of dark and milk chocolate for extra richness. They turned out soft and chewy. Who wants the recipe?",
      image: cookieImage,
    },
    {
      time: "Tue 8:00 AM",
      user: "Grill Master",
      message: "Fired up the grill for some barbecue ribs last night. Slow-cooked to perfection with a smoky barbecue glaze. The result? Fall-off-the-bone goodness!",
    },
  ];


  const volunteerData = [
    {
      time: "Fri 3:15, 1 week ago",
      user: "John Smith",
      message: "Spent the day volunteering at the local animal shelter. It was heartwarming to see the animals find loving homes. #Volunteer #AnimalShelter",
      image: volunteerImage1,
    },
    {
      time: "Thu 10:45, 2 weeks ago",
      user: "Emily Rodriguez",
      message: "Had a fantastic time helping out at the community garden. We planted vegetables and flowers to beautify our neighborhood. 🌱🌸 #CommunityGarden #Volunteer",
    },
    {
      time: "Wed 2:30, 3 weeks ago",
      user: "Alex Thompson",
      message: "Spent the afternoon assisting at the local food bank. It's incredible to see the impact we can make when we come together to fight hunger. #FoodBank #Volunteer",
    },
    {
      time: "Tue 4:20, 1 month ago",
      user: "Sophia Chen",
      message: "Volunteered at the senior center today, playing games and chatting with the elderly residents. It's so important to bring joy to their lives. #SeniorCenter #Volunteering",
      image: volunteerImage4,
    },
  ];


  const paintingData = [
    {
      time: "Fri 10:15, 1 day ago",
      user: "Emily Turner",
      message: "Just finished a breathtaking landscape painting using acrylics. The vibrant colors and intricate details bring the scene to life!",
    },
    {
      time: "Thu 3:22, 2 days ago",
      user: "Alex Rodriguez",
      message: "Experimenting with watercolor techniques today. The way the colors blend and flow on the paper is truly magical. 🎨",
      image: watercolorArt,
    },
    {
      time: "Wed 5:45, 3 days ago",
      user: "Sophie Johnson",
      message: "Started a new portrait series with oil paints. Each stroke captures the essence of the subject, creating a unique and expressive piece.",
    },
    {
      time: "Tue 8:30, 4 days ago",
      user: "David Smith",
      message: "Abstract art session today! It's fascinating to let creativity run wild and see where the brush takes me. #ArtisticFreedom",
      image: abstractArt,
    },
  ];


  const exerciseData = [
    {
      time: "Today, 7:00 AM",
      user: "FitFreak123",
      message: "Just crushed a high-intensity interval training (HIIT) workout! 💪 Feeling energized and ready to take on the day. #FitnessMotivation #HIIT #WorkoutWednesday",
      image: workoutImage,
    },
    {
      time: "Yesterday, 5:30 PM",
      user: "GymExplorer",
      message: "Explored a new workout routine at the gym today. 🏋️‍♂️ Tried some challenging weightlifting exercises and loved the burn! #GymLife #FitGoals",
    },
    {
      time: "2 days ago, 6:45 AM",
      user: "YogaEnthusiast",
      message: "Started my day with a calming yoga session. 🧘‍♀️ Finding balance both physically and mentally. #YogaLife #MorningRoutine",
      image: yogaPose,
    },
  ];
  const [isSidebarVisible, setIsSidebarVisible] = useState(false);

  const toggleSidebar = () => {
    setIsSidebarVisible(!isSidebarVisible);
  };

  const closeSidebar = () => {
    setIsSidebarVisible(false);
  };
  const [isDashboardOpen, setIsDashboardOpen] = useState(false);

  const toggleDashboard = () => {
    setIsDashboardOpen(!isDashboardOpen);
  };

  return (
    <div className=''>
      <nav className="bg-white border-gray-200 dark:bg-primary-300">
        <div className="flex flex-wrap justify-between items-center mx-auto max-w-screen-xl p-4">
          <a href="https://flowbite.com" className="flex items-center space-x-3 rtl:space-x-reverse">
            <img src={logo} className="h-6" alt="Flowbite Logo" />
          </a>
          <div className="flex items-center space-x-6 rtl:space-x-reverse">
            <button className="gap-8 rounded bg-secondary-500 p-2 hover:bg-primary-500 hover:text-white w-[150px] " onClick={toggleSidebar}>Community</button>
            <button className="gap-8 rounded bg-secondary-500 p-2 hover:bg-primary-500 hover:text-white w-[150px] " onClick={toggleDashboard}>Notifications</button>
          </div>
        </div>
      </nav>
      <div className="flex flex-row bg-primary-100 h-screen">

        {/* ------------------------------Left----------------------- */}
        <div>

          <div
            className={`fixed left-0 top-0 h-screen w-[15rem] bg-white transition-transform duration-300 transform ${isSidebarVisible ? 'translate-x-0' : '-translate-x-full'
              }`}
          >

            <div className="w-[15rem] bg-white h-screen">
              <NavLink to='/home'><button type="button" className="w-full flex items-center justify-center w-1/2 px-5 py-2 text-sm text-gray-700 transition-colors duration-200 bg-white gap-x-2 sm:w-auto mb-4">
                <svg className="w-5 h-5 rtl:rotate-180" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M6.75 15.75L3 12m0 0l3.75-3.75M3 12h18" />
                </svg>
                <span>Go back</span>
              </button></NavLink>
              <div className="flex p-2 w-[80%] m-2 bg-primary-100 rounded-sm items-center justify-items-center place-content-center">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6">
                  <path strokeLinecap="round" strokeLinejoin="round" d="M20.25 8.511c.884.284 1.5 1.128 1.5 2.097v4.286c0 1.136-.847 2.1-1.98 2.193-.34.027-.68.052-1.02.072v3.091l-3-3c-1.354 0-2.694-.055-4.02-.163a2.115 2.115 0 01-.825-.242m9.345-8.334a2.126 2.126 0 00-.476-.095 48.64 48.64 0 00-8.048 0c-1.131.094-1.976 1.057-1.976 2.192v4.286c0 .837.46 1.58 1.155 1.951m9.345-8.334V6.637c0-1.621-1.152-3.026-2.76-3.235A48.455 48.455 0 0011.25 3c-2.115 0-4.198.137-6.24.402-1.608.209-2.76 1.614-2.76 3.235v6.226c0 1.621 1.152 3.026 2.76 3.235.577.075 1.157.14 1.74.194V21l4.155-4.155" />
                </svg>

                <h1 className="pl-2 text-[1.2rem]">My Forums</h1>
              </div>



              <div className="mt-12 space-y-4">
                <div className="flex p-2 w-[80%] m-2 bg-white border-2 border-primary-100 rounded-sm items-center hover:bg-primary-100" onClick={Exercise}>
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6">
                    <path strokeLinecap="round" strokeLinejoin="round" d="M15 19.128a9.38 9.38 0 002.625.372 9.337 9.337 0 004.121-.952 4.125 4.125 0 00-7.533-2.493M15 19.128v-.003c0-1.113-.285-2.16-.786-3.07M15 19.128v.106A12.318 12.318 0 018.624 21c-2.331 0-4.512-.645-6.374-1.766l-.001-.109a6.375 6.375 0 0111.964-3.07M12 6.375a3.375 3.375 0 11-6.75 0 3.375 3.375 0 016.75 0zm8.25 2.25a2.625 2.625 0 11-5.25 0 2.625 2.625 0 015.25 0z" />
                  </svg>


                  <h1 className="pl-2">Exercise</h1>
                </div>

                <div className="flex p-2 w-[80%] m-2 bg-white border-2 border-primary-100 rounded-sm items-center hover:bg-primary-100" onClick={Painting}>
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6">
                    <path strokeLinecap="round" strokeLinejoin="round" d="M9.53 16.122a3 3 0 00-5.78 1.128 2.25 2.25 0 01-2.4 2.245 4.5 4.5 0 008.4-2.245c0-.399-.078-.78-.22-1.128zm0 0a15.998 15.998 0 003.388-1.62m-5.043-.025a15.994 15.994 0 011.622-3.395m3.42 3.42a15.995 15.995 0 004.764-4.648l3.876-5.814a1.151 1.151 0 00-1.597-1.597L14.146 6.32a15.996 15.996 0 00-4.649 4.763m3.42 3.42a6.776 6.776 0 00-3.42-3.42" />
                  </svg>


                  <h1 className="pl-2">Painting</h1>
                </div>

                <div className="flex p-2 w-[80%] m-2 bg-white border-2 border-primary-100 rounded-sm items-center hover:bg-primary-100" onClick={Volunteer}>
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6">
                    <path strokeLinecap="round" strokeLinejoin="round" d="M10.34 15.84c-.688-.06-1.386-.09-2.09-.09H7.5a4.5 4.5 0 110-9h.75c.704 0 1.402-.03 2.09-.09m0 9.18c.253.962.584 1.892.985 2.783.247.55.06 1.21-.463 1.511l-.657.38c-.551.318-1.26.117-1.527-.461a20.845 20.845 0 01-1.44-4.282m3.102.069a18.03 18.03 0 01-.59-4.59c0-1.586.205-3.124.59-4.59m0 9.18a23.848 23.848 0 018.835 2.535M10.34 6.66a23.847 23.847 0 008.835-2.535m0 0A23.74 23.74 0 0018.795 3m.38 1.125a23.91 23.91 0 011.014 5.395m-1.014 8.855c-.118.38-.245.754-.38 1.125m.38-1.125a23.91 23.91 0 001.014-5.395m0-3.46c.495.413.811 1.035.811 1.73 0 .695-.316 1.317-.811 1.73m0-3.46a24.347 24.347 0 010 3.46" />
                  </svg>


                  <h1 className="pl-2">Volunteering</h1>
                </div>


                <div className="flex p-2 w-[80%] m-2 bg-white border-2 border-primary-100 rounded-sm items-center hover:bg-primary-100" onClick={Cooking}>
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6">
                    <path strokeLinecap="round" strokeLinejoin="round" d="M15.362 5.214A8.252 8.252 0 0112 21 8.25 8.25 0 016.038 7.048 8.287 8.287 0 009 9.6a8.983 8.983 0 013.361-6.867 8.21 8.21 0 003 2.48z" />
                    <path strokeLinecap="round" strokeLinejoin="round" d="M12 18a3.75 3.75 0 00.495-7.467 5.99 5.99 0 00-1.925 3.546 5.974 5.974 0 01-2.133-1A3.75 3.75 0 0012 18z" />
                  </svg>


                  <h1 className="pl-2">Cooking</h1>
                </div>


                <div className="flex p-2 w-[80%] m-2 bg-white border-2 border-primary-100 rounded-sm items-center hover:bg-primary-100" onClick={Cycling}>
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6">
                    <path strokeLinecap="round" strokeLinejoin="round" d="M9 6.75V15m6-6v8.25m.503 3.498l4.875-2.437c.381-.19.622-.58.622-1.006V4.82c0-.836-.88-1.38-1.628-1.006l-3.869 1.934c-.317.159-.69.159-1.006 0L9.503 3.252a1.125 1.125 0 00-1.006 0L3.622 5.689C3.24 5.88 3 6.27 3 6.695V19.18c0 .836.88 1.38 1.628 1.006l3.869-1.934c.317-.159.69-.159 1.006 0l4.994 2.497c.317.158.69.158 1.006 0z" />
                  </svg>


                  <h1 className="pl-2">Cycling</h1>
                </div>



              </div>

            </div>
          </div>
        </div>
        {/* -----------------------------------center------------------------- */}
        {exercise && (
          <div className='pl-12 pt-9 space-y-4 grid justify-items-center ' style={{ width: '100%', overflowY: 'auto', maxHeight: 'calc(100vh - 50px)' }}>
            {/* Map over the array and render a Card component for each object */}
            {exerciseData.map((cardProps, index) => (
              <Card key={index} {...cardProps} />
            ))}
          </div>
        )}

        {cycling && (
          <div className='pl-12 pt-9 space-y-4 grid justify-items-center ' style={{ width: '100%', overflowY: 'auto', maxHeight: 'calc(100vh - 50px)' }}>
            {/* Map over the array and render a Card component for each object */}
            {cyclingCardData.map((cardProps, index) => (
              <Card key={index} {...cardProps} />
            ))}
          </div>
        )}

        {painting && (
          <div className='pl-12 pt-9 space-y-4 grid justify-items-center ' style={{ width: '100%', overflowY: 'auto', maxHeight: 'calc(100vh - 50px)' }}>
            {/* Map over the array and render a Card component for each object */}
            {paintingData.map((cardProps, index) => (
              <Card key={index} {...cardProps} />
            ))}
          </div>
        )}

        {cooking && (
          <div className='pl-12 pt-9 space-y-4 grid justify-items-center ' style={{ width: '100%', overflowY: 'auto', maxHeight: 'calc(100vh - 50px)' }}>
            {/* Map over the array and render a Card component for each object */}
            {cookingCardData.map((cardProps, index) => (
              <Card key={index} {...cardProps} />
            ))}
          </div>
        )}

        {volunteer && (
          <div className='pl-12 pt-9 space-y-4 grid justify-items-center ' style={{ width: '100%', overflowY: 'auto', maxHeight: 'calc(100vh - 50px)' }}>
            {/* Map over the array and render a Card component for each object */}
            {volunteerData.map((cardProps, index) => (
              <Card key={index} {...cardProps} />
            ))}
          </div>
        )}
      </div>

      {/* -----------------------------------right------------------------- */}
      <div>
        {isDashboardOpen && (
          <div className="absolute top-0 right-0 w-[20rem] bg-white h-screen">
            <div className='flex items-center space-x-32'>
              <h1 className="ml-[50px] mt-[25px] text-[1.2rem] underline underline-offset-4">Notifications</h1>
              <div onClick={toggleDashboard}>
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6">
                  <path strokeLinecap="round" strokeLinejoin="round" d="M6 18L18 6M6 6l12 12" />
                </svg>
              </div>
            </div>
            <div className="mt-2">

              <div id="toast-notification" className="w-full max-w-xs p-4 text-gray-900 bg-white rounded-lg shadow " role="alert">
                <div className="flex items-center">
                  <div className="relative inline-block shrink-0">
                    <img className="w-12 h-12 rounded-full" src={user} alt="Jese Leos image" />
                  </div>
                  <div className="ms-3 text-sm font-normal">
                    <div className="text-sm font-semibold text-gray-900">Raj Thakhur</div>
                    <div className="text-sm font-normal">commmented on your photo</div>
                    <span className="text-xs font-medium text-blue-600 dark:text-blue-500">few seconds ago</span>
                  </div>
                </div>
              </div>


              <div id="toast-notification" className="w-full max-w-xs p-4 text-gray-900 bg-white rounded-lg shadow " role="alert">
                <div className="flex items-center">
                  <div className="relative inline-block shrink-0">
                    <img className="w-12 h-12 rounded-full" src={user} alt="Jese Leos image" />
                  </div>
                  <div className="ms-3 text-sm font-normal">
                    <div className="text-sm font-semibold text-gray-900">Raj Thakhur</div>
                    <div className="text-sm font-normal">replied to you</div>
                    <span className="text-xs font-medium text-blue-600 dark:text-blue-500">5 mins ago</span>
                  </div>
                </div>
              </div>

              <div id="toast-notification" className="w-full max-w-xs p-4 text-gray-900 bg-white rounded-lg shadow " role="alert">
                <div className="flex items-center">
                  <div className="relative inline-block shrink-0">
                    <img className="w-12 h-12 rounded-full" src={user2} alt="Jese Leos image" />
                  </div>
                  <div className="ms-3 text-sm font-normal">
                    <div className="text-sm font-semibold text-gray-900">Shreya Mishra</div>
                    <div className="text-sm font-normal">Shared a post</div>
                    <span className="text-xs font-medium text-blue-600 dark:text-blue-500">30 mins ago</span>
                  </div>
                </div>
              </div>



              <div id="toast-notification" className="w-full max-w-xs p-4 text-gray-900 bg-white rounded-lg shadow " role="alert">
                <div className="flex items-center">
                  <div className="relative inline-block shrink-0">
                    <img className="w-12 h-12 rounded-full" src={user3} alt="Jese Leos image" />
                  </div>
                  <div className="ms-3 text-sm font-normal">
                    <div className="text-sm font-semibold text-gray-900">Kiran Gupta</div>
                    <div className="text-sm font-normal">Tagged you in a post</div>
                    <span className="text-xs font-medium text-blue-600 dark:text-blue-500">1 week ago</span>
                  </div>
                </div>
              </div>


            </div>
          </div>
        )}
      </div>
    </div>

  )
}

export default community
