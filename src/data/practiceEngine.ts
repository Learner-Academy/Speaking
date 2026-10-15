// ============================================================================
// SPEECH PRACTICE DATA ENGINE (DAY-AWARE MULTI-DIMENSIONAL RETRIEVAL)
// ============================================================================

export type AgeGroup = '4-6' | '7-9' | '10-12' | '13-16';
export type Level = 'Beginner' | 'Intermediate' | 'Advanced';

export interface PracticeCardItem {
  id: string; // e.g., "cat-1_top-3_d-11"
  categoryId: string | number;
  topicId: string | number;
  day: number; // 1 to 90
  ageGroup: AgeGroup;
  level: Level;
  practiceItems: [string, string, string]; // Strictly 3 speaking items
  phoneticHint?: string; // Optional pronunciation cue
}

export interface TopicLexicon {
  categoryIndex: number;
  categoryName: string;
  topicIndex: number;
  slug: string;
  name: string;
  phonetic: string;
  // Core single words for 4-6 Day 1 & atomic assembly
  words: string[];
  singleWordAdjectives: string[];
  // 2-word functional chunks (Agent + Action, Modifier + Noun) - Days 2-7
  chunks2w: [string, string, string][];
  // 3-word short phrases (Subject + Verb + Object) - Days 8-14
  phrases3w: [string, string, string][];
  // 4-word functional sentences - Days 15-21
  sentences4w: [string, string, string][];
  // 5-word expressive conversational sentences - Days 22-30
  sentences5w: [string, string, string][];
  // Thematic entities & action verbs for algorithmic day synthesis
  entities: string[];
  actions: string[];
  descriptors: string[];
  situationalContexts: string[];
  idioms: string[];
  academicThemes: string[];
}

export const CATEGORY_NAMES: string[] = [
  'Home & Daily Life',
  'Family & Relatives',
  'Travel & Transport',
  'Shopping & Food',
  'Health & Doctor',
  'School & Study',
  'Friends & Play',
  'Nature & Outdoors',
  'Manners & Help',
  'Fun & Tech',
  'Time & Weather',
  'Holidays & Events',
  'Sports & Games',
  'Clothes & Style',
  'Chores & Helping',
];

const TOPIC_REGISTRY: Record<string, TopicLexicon> = {};

const TOPIC_METADATA_LIST: Array<{ slug: string; name: string; catIdx: number; catName: string; words: string[]; entity: string; action: string }> = [
  // Category 1: Home & Daily Life (6 topics)
  { slug: 'breakfast-chat', name: 'Breakfast Chat', catIdx: 1, catName: 'Home & Daily Life', words: ['Milk', 'Toast', 'Juice', 'Bread', 'Water', 'Apple', 'Honey', 'Eggs', 'Plate', 'Spoon'], entity: 'toast', action: 'pass' },
  { slug: 'lunch-dinner', name: 'Lunch & Dinner', catIdx: 1, catName: 'Home & Daily Life', words: ['Soup', 'Rice', 'Pasta', 'Salad', 'Bread', 'Fish', 'Beans', 'Fork', 'Bowl', 'Water'], entity: 'soup', action: 'serve' },
  { slug: 'kitchen-help', name: 'Kitchen Help', catIdx: 1, catName: 'Home & Daily Life', words: ['Wash', 'Stir', 'Spoon', 'Pot', 'Bowl', 'Wipe', 'Fruit', 'Peel', 'Towel', 'Clean'], entity: 'dish', action: 'rinse' },
  { slug: 'bedtime-stories', name: 'Bedtime Stories', catIdx: 1, catName: 'Home & Daily Life', words: ['Book', 'Moon', 'Bed', 'Sleep', 'Dream', 'Pillow', 'Night', 'Star', 'Story', 'Cozy'], entity: 'storybook', action: 'read' },
  { slug: 'morning-talk', name: 'Morning Talk', catIdx: 1, catName: 'Home & Daily Life', words: ['Sun', 'Rise', 'Smile', 'Brush', 'Teeth', 'Shirt', 'Bag', 'Ready', 'Day', 'Happy'], entity: 'morning sun', action: 'greet' },
  { slug: 'evening-tea', name: 'Evening Tea', catIdx: 1, catName: 'Home & Daily Life', words: ['Tea', 'Cup', 'Warm', 'Sit', 'Chat', 'Cookie', 'Relax', 'Quiet', 'Herbal', 'Sip'], entity: 'warm tea', action: 'sip' },

  // Category 2: Family & Relatives (5 topics)
  { slug: 'mom-and-dad', name: 'Mom & Dad', catIdx: 2, catName: 'Family & Relatives', words: ['Mom', 'Dad', 'Hug', 'Love', 'Help', 'Smile', 'Family', 'Care', 'Heart', 'Together'], entity: 'parents', action: 'hug' },
  { slug: 'grandparents-chat', name: 'Grandparents Chat', catIdx: 2, catName: 'Family & Relatives', words: ['Grandma', 'Grandpa', 'Story', 'Wisdom', 'Hug', 'Old', 'Tea', 'Memory', 'Laugh', 'Love'], entity: 'grandparents', action: 'listen' },
  { slug: 'morning-with-aunt', name: 'Morning with Aunt', catIdx: 2, catName: 'Family & Relatives', words: ['Aunt', 'Visit', 'News', 'Walk', 'Smile', 'Guest', 'Welcome', 'Talk', 'Gift', 'Joy'], entity: 'aunt', action: 'welcome' },
  { slug: 'dinner-with-uncle', name: 'Dinner with Uncle', catIdx: 2, catName: 'Family & Relatives', words: ['Uncle', 'Joke', 'Dine', 'Laugh', 'Story', 'Dessert', 'Weekend', 'Cheer', 'Table', 'Kin'], entity: 'uncle', action: 'converse' },
  { slug: 'big-feelings', name: 'Big Feelings', catIdx: 2, catName: 'Family & Relatives', words: ['Calm', 'Breathe', 'Happy', 'Kind', 'Patient', 'Peace', 'Gentle', 'Listen', 'Share', 'Care'], entity: 'feelings', action: 'express' },

  // Category 3: Travel & Transport (5 topics)
  { slug: 'bus-station', name: 'Bus Station', catIdx: 3, catName: 'Travel & Transport', words: ['Bus', 'Stop', 'Ticket', 'Ride', 'Driver', 'Seat', 'Travel', 'Route', 'Road', 'Arrive'], entity: 'city bus', action: 'board' },
  { slug: 'train-tickets', name: 'Train Tickets', catIdx: 3, catName: 'Travel & Transport', words: ['Train', 'Track', 'Ticket', 'Rail', 'Express', 'Board', 'Travel', 'Station', 'Speed', 'Seat'], entity: 'passenger train', action: 'travel' },
  { slug: 'in-a-taxi', name: 'In a Taxi', catIdx: 3, catName: 'Travel & Transport', words: ['Taxi', 'Cab', 'Driver', 'Belt', 'Ride', 'Street', 'Turn', 'Meter', 'Drive', 'Corner'], entity: 'yellow cab', action: 'ride' },
  { slug: 'airplane-flight', name: 'Airplane Flight', catIdx: 3, catName: 'Travel & Transport', words: ['Plane', 'Fly', 'Gate', 'Wing', 'Cloud', 'Sky', 'Seat', 'Pilot', 'Belt', 'Travel'], entity: 'airplane', action: 'fly' },
  { slug: 'asking-directions', name: 'Asking Directions', catIdx: 3, catName: 'Travel & Transport', words: ['Map', 'Way', 'Turn', 'Left', 'Right', 'Straight', 'Street', 'Walk', 'Guide', 'Corner'], entity: 'street map', action: 'navigate' },

  // Category 4: Shopping & Food (6 topics)
  { slug: 'grocery-store', name: 'Grocery Store', catIdx: 4, catName: 'Shopping & Food', words: ['Shop', 'Cart', 'Fruit', 'Veggie', 'Milk', 'Bread', 'Aisle', 'Pick', 'Fresh', 'Store'], entity: 'grocery cart', action: 'shop' },
  { slug: 'buying-toys', name: 'Buying Toys', catIdx: 4, catName: 'Shopping & Food', words: ['Toy', 'Puzzle', 'Bear', 'Block', 'Game', 'Fun', 'Choose', 'Play', 'Store', 'Gift'], entity: 'wooden puzzle', action: 'choose' },
  { slug: 'paying-cashier', name: 'Paying Cashier', catIdx: 4, catName: 'Shopping & Food', words: ['Pay', 'Cashier', 'Receipt', 'Card', 'Count', 'Money', 'Smile', 'Bag', 'Price', 'Change'], entity: 'receipt', action: 'pay' },
  { slug: 'ordering-snacks', name: 'Ordering Snacks', catIdx: 4, catName: 'Shopping & Food', words: ['Snack', 'Juice', 'Bar', 'Treat', 'Order', 'Crisp', 'Sweet', 'Taste', 'Share', 'Menu'], entity: 'fruit bar', action: 'order' },
  { slug: 'street-food', name: 'Street Food', catIdx: 4, catName: 'Shopping & Food', words: ['Food', 'Cart', 'Skewer', 'Smell', 'Hot', 'Pastry', 'Treat', 'Taste', 'Steam', 'Bite'], entity: 'warm pastry', action: 'taste' },
  { slug: 'table-booking', name: 'Table Booking', catIdx: 4, catName: 'Shopping & Food', words: ['Table', 'Book', 'Reserve', 'Dinner', 'Menu', 'Four', 'Seat', 'Host', 'Window', 'Visit'], entity: 'table reservation', action: 'reserve' },

  // Category 5: Health & Doctor (5 topics)
  { slug: 'feeling-sick', name: 'Feeling Sick', catIdx: 5, catName: 'Health & Doctor', words: ['Rest', 'Water', 'Care', 'Warm', 'Heal', 'Bed', 'Blanket', 'Quiet', 'Safe', 'Doctor'], entity: 'comforting rest', action: 'recover' },
  { slug: 'at-the-clinic', name: 'At the Clinic', catIdx: 5, catName: 'Health & Doctor', words: ['Doctor', 'Nurse', 'Pulse', 'Heart', 'Coat', 'Breathe', 'Check', 'Clinic', 'Care', 'Health'], entity: 'stethoscope', action: 'examine' },
  { slug: 'pharmacy-visit', name: 'Pharmacy Visit', catIdx: 5, catName: 'Health & Doctor', words: ['Pill', 'Drop', 'Vitamin', 'Bottle', 'Medicine', 'Advice', 'Care', 'Dose', 'Heal', 'Safe'], entity: 'vitamins', action: 'prescribe' },
  { slug: 'describing-pain', name: 'Describing Pain', catIdx: 5, catName: 'Health & Doctor', words: ['Hurt', 'Rest', 'Head', 'Tummy', 'Throat', 'Calm', 'Care', 'Explain', 'Heal', 'Better'], entity: 'symptom description', action: 'explain' },
  { slug: 'comforting-family', name: 'Comforting Family', catIdx: 5, catName: 'Health & Doctor', words: ['Hug', 'Hold', 'Kind', 'Water', 'Smile', 'Cheer', 'Love', 'Stay', 'Help', 'Peace'], entity: 'warm hug', action: 'comfort' },

  // Category 6: School & Study (5 topics)
  { slug: 'greeting-teachers', name: 'Greeting Teachers', catIdx: 6, catName: 'School & Study', words: ['Teacher', 'Hello', 'Bow', 'Morning', 'School', 'Class', 'Smile', 'Polite', 'Learn', 'Desk'], entity: 'morning greeting', action: 'greet' },
  { slug: 'homework-help', name: 'Homework Help', catIdx: 6, catName: 'School & Study', words: ['Pencil', 'Book', 'Math', 'Read', 'Solve', 'Page', 'Learn', 'Write', 'Notebook', 'Think'], entity: 'homework notebook', action: 'solve' },
  { slug: 'classroom-chat', name: 'Classroom Chat', catIdx: 6, catName: 'School & Study', words: ['Hand', 'Ask', 'Desk', 'Share', 'Class', 'Listen', 'Learn', 'Speak', 'Partner', 'Friend'], entity: 'classroom discussion', action: 'participate' },
  { slug: 'playground-bell', name: 'Playground Bell', catIdx: 6, catName: 'School & Study', words: ['Bell', 'Recess', 'Play', 'Yard', 'Line', 'Tag', 'Run', 'Air', 'Game', 'Cheer'], entity: 'recess bell', action: 'play' },
  { slug: 'group-projects', name: 'Group Projects', catIdx: 6, catName: 'School & Study', words: ['Team', 'Poster', 'Marker', 'Idea', 'Share', 'Plan', 'Build', 'Show', 'Together', 'Learn'], entity: 'team presentation', action: 'collaborate' },

  // Category 7: Friends & Play (5 topics)
  { slug: 'making-friends', name: 'Making Friends', catIdx: 7, catName: 'Friends & Play', words: ['Friend', 'Hello', 'Name', 'Smile', 'Wave', 'Play', 'Share', 'Talk', 'Kind', 'Joy'], entity: 'friendly introduction', action: 'introduce' },
  { slug: 'birthday-party', name: 'Birthday Party', catIdx: 7, catName: 'Friends & Play', words: ['Cake', 'Candle', 'Hat', 'Party', 'Sing', 'Gift', 'Wish', 'Cheer', 'Balloon', 'Fun'], entity: 'birthday cake', action: 'celebrate' },
  { slug: 'sharing-toys', name: 'Sharing Toys', catIdx: 7, catName: 'Friends & Play', words: ['Share', 'Turn', 'Toy', 'Block', 'Kind', 'Game', 'Together', 'Smile', 'Give', 'Fair'], entity: 'shared toy', action: 'share' },
  { slug: 'playground-games', name: 'Playground Games', catIdx: 7, catName: 'Friends & Play', words: ['Slide', 'Swing', 'Tag', 'Run', 'Chase', 'Jump', 'Catch', 'Ball', 'Laugh', 'Sand'], entity: 'playground swing', action: 'play' },
  { slug: 'inviting-a-friend', name: 'Inviting a Friend', catIdx: 7, catName: 'Friends & Play', words: ['Invite', 'Visit', 'Come', 'Park', 'Play', 'House', 'Weekend', 'Board', 'Game', 'Welcome'], entity: 'friendly invitation', action: 'invite' },

  // Category 8: Nature & Outdoors (5 topics)
  { slug: 'park-walks', name: 'Park Walks', catIdx: 8, catName: 'Nature & Outdoors', words: ['Tree', 'Grass', 'Bird', 'Walk', 'Bench', 'Sun', 'Leaf', 'Flower', 'Path', 'Air'], entity: 'park trail', action: 'stroll' },
  { slug: 'rainy-days', name: 'Rainy Days', catIdx: 8, catName: 'Nature & Outdoors', words: ['Rain', 'Boot', 'Puddle', 'Splash', 'Cloud', 'Umbrella', 'Drop', 'Wet', 'Sky', 'Coat'], entity: 'rain umbrella', action: 'splash' },
  { slug: 'pet-animals', name: 'Pet Animals', catIdx: 8, catName: 'Nature & Outdoors', words: ['Dog', 'Cat', 'Pet', 'Tail', 'Puppy', 'Bowl', 'Bark', 'Soft', 'Fur', 'Play'], entity: 'friendly puppy', action: 'care' },
  { slug: 'beach-fun', name: 'Beach Fun', catIdx: 8, catName: 'Nature & Outdoors', words: ['Sand', 'Wave', 'Shell', 'Beach', 'Castle', 'Sea', 'Sun', 'Towel', 'Water', 'Crab'], entity: 'sandcastle', action: 'build' },
  { slug: 'camping-trip', name: 'Camping Trip', catIdx: 8, catName: 'Nature & Outdoors', words: ['Tent', 'Fire', 'Star', 'Camp', 'Campfire', 'Bag', 'Flashlight', 'Night', 'Glow', 'Woods'], entity: 'camping tent', action: 'camp' },

  // Category 9: Manners & Help (5 topics)
  { slug: 'saying-thank-you', name: 'Saying Thank You', catIdx: 9, catName: 'Manners & Help', words: ['Thanks', 'Grateful', 'Kind', 'Polite', 'Smile', 'Nod', 'Heart', 'Grace', 'Help', 'Warm'], entity: 'expression of gratitude', action: 'thank' },
  { slug: 'saying-sorry', name: 'Saying Sorry', catIdx: 9, catName: 'Manners & Help', words: ['Sorry', 'Gentle', 'Hug', 'Kind', 'Fix', 'Truth', 'Honest', 'Peace', 'Care', 'Friend'], entity: 'sincere apology', action: 'apologize' },
  { slug: 'asking-for-help', name: 'Asking for Help', catIdx: 9, catName: 'Manners & Help', words: ['Help', 'Please', 'Reach', 'Guide', 'Team', 'Show', 'Ask', 'Hand', 'Solve', 'Kindly'], entity: 'polite request', action: 'request' },
  { slug: 'lost-in-public', name: 'Lost in Public', catIdx: 9, catName: 'Manners & Help', words: ['Safe', 'Calm', 'Officer', 'Booth', 'Name', 'Phone', 'Help', 'Stay', 'Wait', 'Reunion'], entity: 'safety plan', action: 'navigate' },
  { slug: 'polite-requests', name: 'Polite Requests', catIdx: 9, catName: 'Manners & Help', words: ['Please', 'Kindly', 'Pass', 'Excuse', 'Thanks', 'Gentle', 'Courtesy', 'Smile', 'Thank', 'Nod'], entity: 'courteous inquiry', action: 'inquire' },

  // Category 10: Fun & Tech (5 topics)
  { slug: 'video-games', name: 'Video Games', catIdx: 10, catName: 'Fun & Tech', words: ['Game', 'Score', 'Level', 'Jump', 'Play', 'Screen', 'Quest', 'Team', 'Win', 'Challenge'], entity: 'game controller', action: 'play' },
  { slug: 'cartoon-talk', name: 'Cartoon Talk', catIdx: 10, catName: 'Fun & Tech', words: ['Toon', 'Laugh', 'Hero', 'Magic', 'Frame', 'Story', 'Fun', 'Comic', 'Color', 'Voice'], entity: 'animated character', action: 'watch' },
  { slug: 'drawing-colors', name: 'Drawing Colors', catIdx: 10, catName: 'Fun & Tech', words: ['Draw', 'Crayon', 'Paint', 'Color', 'Paper', 'Brush', 'Red', 'Blue', 'Art', 'Sketch'], entity: 'colorful sketchbook', action: 'draw' },
  { slug: 'phone-calls', name: 'Phone Calls', catIdx: 10, catName: 'Fun & Tech', words: ['Phone', 'Ring', 'Hello', 'Speak', 'Hear', 'Voice', 'Call', 'Clear', 'Chat', 'Bye'], entity: 'telephone call', action: 'converse' },
  { slug: 'video-chats', name: 'Video Chats', catIdx: 10, catName: 'Fun & Tech', words: ['Cam', 'Screen', 'Wave', 'Mic', 'Smile', 'Online', 'See', 'Talk', 'Chat', 'Connect'], entity: 'video conference', action: 'connect' },

  // Category 11: Time & Weather (5 topics)
  { slug: 'telling-time', name: 'Telling Time', catIdx: 11, catName: 'Time & Weather', words: ['Clock', 'Hour', 'Minute', 'Hand', 'Time', 'Tick', 'Tock', 'Twelve', 'Watch', 'Alarm'], entity: 'wall clock', action: 'measure' },
  { slug: 'todays-weather', name: 'Today\'s Weather', catIdx: 11, catName: 'Time & Weather', words: ['Sun', 'Cloud', 'Wind', 'Sky', 'Rain', 'Warm', 'Cool', 'Day', 'Forecast', 'Breeze'], entity: 'weather forecast', action: 'observe' },
  { slug: 'hot-and-cold-days', name: 'Hot and Cold Days', catIdx: 11, catName: 'Time & Weather', words: ['Hot', 'Cold', 'Sweater', 'Ice', 'Heat', 'Sun', 'Chill', 'Water', 'Season', 'Breeze'], entity: 'seasonal weather', action: 'adapt' },
  { slug: 'morning-routine', name: 'Morning Routine', catIdx: 11, catName: 'Time & Weather', words: ['Alarm', 'Wake', 'Wash', 'Brush', 'Dress', 'Bag', 'Shoes', 'Ready', 'Step', 'Clock'], entity: 'morning schedule', action: 'organize' },
  { slug: 'night-sky', name: 'Night Sky', catIdx: 11, catName: 'Time & Weather', words: ['Moon', 'Star', 'Night', 'Dark', 'Glow', 'Sky', 'Shine', 'Constellation', 'Breeze', 'Quiet'], entity: 'stellar constellation', action: 'gaze' },

  // Category 12: Holidays & Events (5 topics)
  { slug: 'holiday-plans', name: 'Holiday Plans', catIdx: 12, catName: 'Holidays & Events', words: ['Trip', 'Plan', 'Pack', 'Family', 'Calendar', 'Visit', 'Feast', 'Joy', 'Holiday', 'Cheer'], entity: 'vacation itinerary', action: 'plan' },
  { slug: 'festival-greetings', name: 'Festival Greetings', catIdx: 12, catName: 'Holidays & Events', words: ['Light', 'Greet', 'Joy', 'Festival', 'Music', 'Celebrate', 'Peace', 'Cheer', 'Tradition', 'Wish'], entity: 'festival lights', action: 'celebrate' },
  { slug: 'packing-bags', name: 'Packing Bags', catIdx: 12, catName: 'Holidays & Events', words: ['Pack', 'Bag', 'Suitcase', 'Zip', 'Shirt', 'List', 'Ready', 'Tag', 'Fold', 'Luggage'], entity: 'travel suitcase', action: 'pack' },
  { slug: 'happy-new-year', name: 'Happy New Year', catIdx: 12, catName: 'Holidays & Events', words: ['Year', 'New', 'Clock', 'Cheer', 'Wish', 'Sparkle', 'Countdown', 'Midnight', 'Fresh', 'Start'], entity: 'midnight countdown', action: 'toast' },
  { slug: 'birthday-gifts', name: 'Birthday Gifts', catIdx: 12, catName: 'Holidays & Events', words: ['Gift', 'Ribbon', 'Box', 'Surprise', 'Open', 'Smile', 'Cheer', 'Present', 'Wrap', 'Joy'], entity: 'wrapped present', action: 'unbox' },

  // Category 13: Sports & Games (5 topics)
  { slug: 'playing-soccer', name: 'Playing Soccer', catIdx: 13, catName: 'Sports & Games', words: ['Ball', 'Kick', 'Goal', 'Run', 'Pass', 'Team', 'Cleats', 'Field', 'Score', 'Whistle'], entity: 'soccer ball', action: 'kick' },
  { slug: 'swimming-talk', name: 'Swimming Talk', catIdx: 13, catName: 'Sports & Games', words: ['Swim', 'Pool', 'Goggles', 'Stroke', 'Kick', 'Water', 'Splash', 'Dive', 'Towel', 'Breathe'], entity: 'swimming pool', action: 'swim' },
  { slug: 'team-games', name: 'Team Games', catIdx: 13, catName: 'Sports & Games', words: ['Team', 'Pass', 'Cheer', 'Clap', 'Huddle', 'Score', 'Game', 'Win', 'Help', 'Play'], entity: 'team huddle', action: 'cooperate' },
  { slug: 'winning-and-losing', name: 'Winning and Losing', catIdx: 13, catName: 'Sports & Games', words: ['Handshake', 'Respect', 'Fair', 'Play', 'Pride', 'Try', 'Cheer', 'Game', 'Sport', 'Honor'], entity: 'sportsmanship handshake', action: 'honor' },
  { slug: 'riding-a-bike', name: 'Riding a Bike', catIdx: 13, catName: 'Sports & Games', words: ['Bike', 'Helmet', 'Pedal', 'Wheel', 'Balance', 'Road', 'Handle', 'Brake', 'Bell', 'Ride'], entity: 'bicycle helmet', action: 'ride' },

  // Category 14: Clothes & Style (5 topics)
  { slug: 'choosing-clothes', name: 'Choosing Clothes', catIdx: 14, catName: 'Clothes & Style', words: ['Shirt', 'Pants', 'Color', 'Outfit', 'Dress', 'Jacket', 'Wear', 'Neat', 'Choose', 'Clean'], entity: 'cotton shirt', action: 'choose' },
  { slug: 'tying-shoes', name: 'Tying Shoes', catIdx: 14, catName: 'Clothes & Style', words: ['Laces', 'Knot', 'Tie', 'Shoe', 'Loop', 'Sneaker', 'Tight', 'Pull', 'Fit', 'Bow'], entity: 'shoe laces', action: 'tie' },
  { slug: 'washing-face', name: 'Washing Face', catIdx: 14, catName: 'Clothes & Style', words: ['Soap', 'Water', 'Splash', 'Face', 'Towel', 'Clean', 'Cheek', 'Dry', 'Gently', 'Fresh'], entity: 'fresh towel', action: 'wash' },
  { slug: 'getting-dressed', name: 'Getting Dressed', catIdx: 14, catName: 'Clothes & Style', words: ['Button', 'Zip', 'Socks', 'Sweater', 'Wear', 'Fasten', 'Ready', 'Outfit', 'Neat', 'Quick'], entity: 'warm sweater', action: 'dress' },
  { slug: 'shopping-for-shoes', name: 'Shopping for Shoes', catIdx: 14, catName: 'Clothes & Style', words: ['Shoe', 'Fit', 'Size', 'Walk', 'Sneaker', 'Store', 'Try', 'Comfy', 'Sole', 'Pair'], entity: 'running sneakers', action: 'fit' },

  // Category 15: Chores & Helping (5 topics)
  { slug: 'cleaning-the-room', name: 'Cleaning the Room', catIdx: 15, catName: 'Chores & Helping', words: ['Bed', 'Toys', 'Tidy', 'Shelf', 'Floor', 'Clean', 'Room', 'Organize', 'Neat', 'Order'], entity: 'organized bedroom', action: 'tidy' },
  { slug: 'washing-dishes', name: 'Washing Dishes', catIdx: 15, catName: 'Chores & Helping', words: ['Dish', 'Suds', 'Soap', 'Rinse', 'Sponge', 'Dry', 'Clean', 'Sink', 'Rack', 'Plate'], entity: 'dish sponge', action: 'clean' },
  { slug: 'watering-plants', name: 'Watering Plants', catIdx: 15, catName: 'Chores & Helping', words: ['Plant', 'Water', 'Green', 'Leaf', 'Soil', 'Flower', 'Can', 'Garden', 'Pour', 'Sprout'], entity: 'watering can', action: 'water' },
  { slug: 'feeding-pets', name: 'Feeding Pets', catIdx: 15, catName: 'Chores & Helping', words: ['Pet', 'Food', 'Bowl', 'Water', 'Feed', 'Meal', 'Dish', 'Happy', 'Tail', 'Care'], entity: 'pet feeding dish', action: 'feed' },
  { slug: 'folding-clothes', name: 'Folding Clothes', catIdx: 15, catName: 'Chores & Helping', words: ['Fold', 'Shirt', 'Pants', 'Stack', 'Drawer', 'Basket', 'Smooth', 'Neat', 'Laundry', 'Hang'], entity: 'folded laundry', action: 'fold' },
];

// Initialize all 77 topics into TOPIC_REGISTRY
TOPIC_METADATA_LIST.forEach((meta, idx) => {
  const topicIndex = (idx % 6) + 1;
  const w = meta.words;
  const e = meta.entity;
  const a = meta.action;

  const singleWordAdjectives = ['warm', 'good', 'nice', 'clean', 'fresh', 'sweet', 'cool', 'fine'];

  // Days 2-7 chunks (Agent + Action, Modifier + Noun)
  const chunks2w: [string, string, string][] = [
    [`Big ${w[0].toLowerCase()}`, `Good ${w[1].toLowerCase()}`, `${w[2]} now`],
    [`My ${w[0].toLowerCase()}`, `Hold ${w[3].toLowerCase()}`, `Clean ${w[4].toLowerCase()}`],
    [`Warm ${w[5].toLowerCase()}`, `Help ${w[6].toLowerCase()}`, `Safe ${w[7].toLowerCase()}`],
    [`Look ${w[8].toLowerCase()}`, `Nice ${w[9].toLowerCase()}`, `Take ${w[0].toLowerCase()}`],
    [`Find ${w[1].toLowerCase()}`, `Happy ${w[2].toLowerCase()}`, `Go ${w[3].toLowerCase()}`],
    [`Try ${w[4].toLowerCase()}`, `Share ${w[5].toLowerCase()}`, `Great ${w[6].toLowerCase()}`],
  ];

  // Days 8-14 phrases (Subject + Verb + Object)
  const phrases3w: [string, string, string][] = [
    [`I see ${w[0].toLowerCase()}`, `Hold the ${w[1].toLowerCase()}`, `We love ${w[2].toLowerCase()}`],
    [`Show me ${w[3].toLowerCase()}`, `Help with ${w[4].toLowerCase()}`, `Take my ${w[5].toLowerCase()}`],
    [`I like ${w[6].toLowerCase()}`, `Keep it ${w[7].toLowerCase()}`, `We enjoy ${w[8].toLowerCase()}`],
    [`Find the ${w[9].toLowerCase()}`, `Open my ${w[0].toLowerCase()}`, `Share your ${w[1].toLowerCase()}`],
    [`We work together`, `I want ${w[2].toLowerCase()}`, `Look at ${w[3].toLowerCase()}`],
    [`Listen very carefully`, `Clean the ${w[4].toLowerCase()}`, `Give me ${w[5].toLowerCase()}`],
    [`Hold hands nicely`, `Practice with ${w[6].toLowerCase()}`, `We are happy`],
  ];

  // Days 15-21 sentences (4 words)
  const sentences4w: [string, string, string][] = [
    [`I like the ${w[0].toLowerCase()}.`, `Please hold my ${w[1].toLowerCase()}.`, `We practice speaking together.`],
    [`Look at that ${w[2].toLowerCase()}.`, `Can I have ${w[3].toLowerCase()}?`, `We do great work.`],
    [`This is so ${w[4].toLowerCase()}.`, `I love my ${w[5].toLowerCase()}.`, `Share with your friend.`],
    [`Help me with ${w[6].toLowerCase()}.`, `Listen to the teacher.`, `Everything is very ${w[7].toLowerCase()}.`],
    [`We are ready now.`, `Take care of ${w[8].toLowerCase()}.`, `Always smile and learn.`],
    [`Keep the ${w[9].toLowerCase()} safe.`, `We enjoy our day.`, `Practice makes us strong.`],
    [`Thank you for helping.`, `I finished my work.`, `Let us play together.`],
  ];

  // Days 22-30 sentences (5 words)
  const sentences5w: [string, string, string][] = [
    [`I can see the ${w[0].toLowerCase()}.`, `Please pass me that ${w[1].toLowerCase()}.`, `We love our daily practice.`],
    [`May I have some ${w[2].toLowerCase()}?`, `This ${w[3].toLowerCase()} looks very nice.`, `Thank you for your help.`],
    [`We work together as friends.`, `Always take care of ${w[4].toLowerCase()}.`, `I am learning every day.`],
    [`Can you show me that?`, `The ${w[5].toLowerCase()} is very clean.`, `Let us share our things.`],
    [`I finished all my work.`, `Good morning to my friends.`, `We are doing so well.`],
    [`Listen carefully to the instructions.`, `Hold the ${w[6].toLowerCase()} with care.`, `Smile and have great fun.`],
    [`Practice makes our speaking clear.`, `I love exploring new things.`, `Everything looks so wonderful today.`],
    [`We can achieve our goals.`, `Take time to do well.`, `Thank you for being kind.`],
    [`Let us continue our lesson.`, `Speaking practice is so exciting.`, `We are happy and strong.`],
  ];

  TOPIC_REGISTRY[meta.slug] = {
    categoryIndex: meta.catIdx,
    categoryName: meta.catName,
    topicIndex: topicIndex,
    slug: meta.slug,
    name: meta.name,
    phonetic: `/${meta.slug.replace(/-/g, ' ')}/`,
    words: w,
    singleWordAdjectives,
    chunks2w,
    phrases3w,
    sentences4w,
    sentences5w,
    entities: [e, w[0].toLowerCase(), w[1].toLowerCase(), w[2].toLowerCase(), w[3].toLowerCase(), w[4].toLowerCase(), w[5].toLowerCase(), w[6].toLowerCase()],
    actions: [a, 'explore', 'prepare', 'organize', 'coordinate', 'discuss', 'observe', 'celebrate'],
    descriptors: ['wonderful', 'careful', 'thoughtful', 'pleasant', 'collaborative', 'essential', 'constructive', 'helpful', 'orderly', 'harmonious'],
    situationalContexts: ['during our daily routine', 'in the afternoon session', 'with family and peers', 'while learning cooperatively', 'as we navigate new challenges'],
    idioms: ['step up to the plate', 'keep an open mind', 'lend a helping hand', 'hit the mark', 'see eye to eye', 'learn the ropes', 'start on the right foot'],
    academicThemes: ['behavioral cognitive adaptation', 'sociolinguistic pragmatics', 'collaborative communicative competence', 'systematic contextual reflection', 'conceptual synthesis'],
  };
});

// ----------------------------------------------------------------------------
// PRIMARY RETRIEVAL ENGINE
// ----------------------------------------------------------------------------

export function getPracticeContent(
  ageGroup: AgeGroup,
  level: Level,
  day: number,
  categoryId: string | number,
  topicId: string | number
): PracticeCardItem {
  const normalizedDay = Math.max(1, Math.min(90, Math.floor(day) || 1));

  const topicKey = String(topicId || '').trim();
  let lexicon = TOPIC_REGISTRY[topicKey];

  if (!lexicon) {
    const foundSlug = Object.keys(TOPIC_REGISTRY).find(
      (k) => k === topicKey || k.toLowerCase().replace(/[^a-z]/g, '') === topicKey.toLowerCase().replace(/[^a-z]/g, '')
    );
    lexicon = foundSlug ? TOPIC_REGISTRY[foundSlug] : TOPIC_REGISTRY['breakfast-chat'];
  }

  const catNum = typeof categoryId === 'number'
    ? categoryId
    : lexicon.categoryIndex || 1;
  const topNum = typeof topicId === 'number'
    ? topicId
    : lexicon.topicIndex || 1;

  const cardId = `cat-${catNum}_top-${topNum}_d-${normalizedDay}`;

  let items: [string, string, string];

  // ==========================================================================
  // 1. AGE BRACKET: 4-6 (FOUNDATIONAL ORAL MOTOR & SENTENCE EXPANSION)
  // ==========================================================================
  if (ageGroup === '4-6') {
    if (normalizedDay === 1) {
      // Day 1: Single words (strictly 1 word each)
      const w = lexicon.words;
      items = [w[0], w[1], w[2]];
    } else if (normalizedDay >= 2 && normalizedDay <= 7) {
      // Days 2–7: 2-word functional chunks (Agent + Action, Modifier + Noun)
      const chunkBank = lexicon.chunks2w;
      const pair = chunkBank[(normalizedDay - 2) % chunkBank.length];
      items = [pair[0], pair[1], pair[2]];
    } else if (normalizedDay >= 8 && normalizedDay <= 14) {
      // Days 8–14: 3-word short phrases (Subject + Verb + Object)
      const phraseBank = lexicon.phrases3w;
      const trio = phraseBank[(normalizedDay - 8) % phraseBank.length];
      items = [trio[0], trio[1], trio[2]];
    } else if (normalizedDay >= 15 && normalizedDay <= 21) {
      // Days 15–21: 4-word functional sentences
      const sentBank = lexicon.sentences4w;
      const trio = sentBank[(normalizedDay - 15) % sentBank.length];
      items = [trio[0], trio[1], trio[2]];
    } else if (normalizedDay >= 22 && normalizedDay <= 30) {
      // Days 22–30: 5-word expressive conversational sentences
      const sentBank = lexicon.sentences5w;
      const trio = sentBank[(normalizedDay - 22) % sentBank.length];
      items = [trio[0], trio[1], trio[2]];
    } else {
      // Days 31–90: Incremental narrative cadence matched to level
      const d = normalizedDay;
      const w = lexicon.words;
      const adj = lexicon.singleWordAdjectives;
      
      const e1 = w[(d * 7) % w.length].toLowerCase();
      const e2 = w[(d * 5 + 1) % w.length].toLowerCase();
      const e3 = w[(d * 3 + 2) % w.length].toLowerCase();
      const m1 = adj[(d * 2) % adj.length];
      const m2 = adj[(d * 4 + 1) % adj.length];
      const m3 = adj[(d * 6 + 2) % adj.length];
      const mod = d % 3;

      if (level === 'Beginner') {
        // Beginner: Strictly 3-5 words
        if (mod === 0) {
          items = [
            `We eat ${m1} ${e1}.`,        // 4 words
            `I like ${m2} ${e2}.`,        // 4 words
            `Pass the ${m3} ${e3}.`       // 4 words
          ];
        } else if (mod === 1) {
          items = [
            `We enjoy ${m1} ${e1} today.`, // 5 words
            `I drink ${m2} ${e2} happily.`, // 5 words
            `Please pass the ${m3} ${e3}.`  // 5 words
          ];
        } else {
          items = [
            `Taste the ${m1} ${e1} now.`,   // 5 words
            `Look at the ${m2} ${e2}.`,    // 5 words
            `Share some ${m3} ${e3} please.` // 5 words
          ];
        }
      } else if (level === 'Intermediate') {
        // Intermediate: Strictly 4-7 words
        if (mod === 0) {
          items = [
            `Could you pass the ${m1} ${e1}?`,      // 6 words
            `I want some ${m2} ${e2} please.`,      // 6 words
            `We share ${m3} ${e3} together happily.` // 5 words
          ];
        } else if (mod === 1) {
          items = [
            `May I please have ${m1} ${e1}?`,        // 6 words
            `I love having ${m2} ${e2} today.`,      // 6 words
            `We always enjoy our ${m3} ${e3}.`       // 6 words
          ];
        } else {
          items = [
            `Can we eat some ${m1} ${e1}?`,          // 6 words
            `Please give me that ${m2} ${e2}.`,      // 6 words
            `We like learning with ${m3} ${e3}.`     // 6 words
          ];
        }
      } else {
        // Advanced: Strictly 6-9 words
        if (mod === 0) {
          items = [
            `May I please have another ${m1} ${e1}?`,           // 7 words
            `The ${m2} ${e2} tastes sweet and good today.`,     // 8 words
            `I can help clear the ${e3} after eating.`          // 8 words
          ];
        } else if (mod === 1) {
          items = [
            `Could you please pass me the ${m1} ${e1}?`,        // 8 words
            `We always love practicing speaking ${e2} as family.`, // 8 words
            `Thank you for preparing this wonderful ${m3} ${e3}.`  // 8 words
          ];
        } else {
          items = [
            `Would you like to share this ${m1} ${e1}?`,        // 8 words
            `I feel very happy learning about ${m2} ${e2}.`,    // 8 words
            `Everyone enjoys eating delicious ${m3} ${e3} together.` // 7 words
          ];
        }
      }
    }
  }

  // ==========================================================================
  // 2. AGE BRACKET: 7-9 (SYNTACTIC FLUENCY, QUESTIONS, EVERYDAY DIALOGUE)
  // ==========================================================================
  else if (ageGroup === '7-9') {
    const d = normalizedDay;
    const e1 = lexicon.entities[(d * 7) % lexicon.entities.length];
    const e2 = lexicon.entities[(d * 5 + 1) % lexicon.entities.length];
    const act = lexicon.actions[(d * 3) % lexicon.actions.length];
    const desc = lexicon.descriptors[(d * 2) % lexicon.descriptors.length];

    if (level === 'Beginner') {
      const qFrames = [
        `Can you please pass the ${desc} ${e1}?`,
        `What are we planning to do with the ${e2} today?`,
        `Could we check if the ${desc} ${e1} is ready?`,
        `Where should we place the ${e2} after we finish?`,
        `Would you like to explore the ${desc} ${e1} together?`,
        `Could you tell me more about the ${e2}?`,
        `Can we organize the ${desc} ${e1} this afternoon?`,
        `Is there enough time to prepare the ${e2} now?`,
        `Will you show me how to handle the ${desc} ${e1}?`,
        `Could you help me set up the ${e2} nicely?`,
        `Are we going to discuss the ${desc} ${e1} this morning?`,
        `Why is the ${e2} so special to you?`
      ];
      const dFrames = [
        `I really like how we ${act} together every afternoon.`,
        `Our team is excited to observe the ${e1} this week.`,
        `Everyone enjoys learning how to ${act} with patience.`,
        `We are making wonderful progress with the ${e2} today.`,
        `Sharing meals together makes everyone so happy.`,
        `I noticed that working together helps us ${act} much faster.`,
        `We always have fun sharing new ideas about ${e1}.`,
        `It feels great to master new words for the ${e2}.`,
        `Talking with friends gives us great joy.`,
        `We take turns sharing stories around the table.`,
        `Learning together helps everyone understand the ${e1} better.`,
        `Each morning brings a fresh opportunity to ${act} and grow.`,
        `We celebrate every milestone as we speak with ease.`
      ];
      const sFrames = [
        `Let us make sure the ${desc} ${e2} is handled with care.`,
        `I can help you carry the ${e1} whenever you are ready.`,
        `We always remember to use courteous words while practicing.`,
        `Please let me know if you need assistance with the ${e2}.`,
        `Working collaboratively ensures that our goals are met happily.`,
        `I am eager to participate in today's fun activity.`,
        `Taking our time helps us pronounce every word accurately.`,
        `We encourage one another whenever we try something new.`,
        `Let us review what we learned about the ${desc} ${e1}.`,
        `Sharing our thoughts builds stronger friendships every day.`,
        `We are ready to continue with the next exciting activity.`,
        `Listening attentively is just as important as speaking well.`,
        `Our daily consistency is paying off in every conversation.`,
        `Together we make every family moment truly wonderful.`
      ];
      items = [
        qFrames[(d * 7) % qFrames.length],
        dFrames[(d * 5) % dFrames.length],
        sFrames[(d * 3) % sFrames.length]
      ];
    } else if (level === 'Intermediate') {
      const qFrames = [
        `Do we have enough time to ${act} the ${e1} before our next class?`,
        `Could you explain why the ${desc} ${e1} works better in this situation?`,
        `Should we double check the ${e2} before we proceed with the next task?`,
        `Do you think the ${desc} ${e1} will be sufficient for our afternoon presentation?`,
        `How might we coordinate our efforts to ${act} the ${e2} more effectively?`,
        `Would it be beneficial to review the key principles of the ${e1} first?`,
        `Can you show me the most reliable technique to manage the ${desc} ${e2}?`,
        `What strategy should we adopt when we ${act} together tomorrow?`,
        `Is it possible to integrate the ${e1} into our current group project?`,
        `Are there specific guidelines we should follow while handling the ${desc} ${e2}?`,
        `Could we deliberate on the best way to ${act} the ${e1} today?`,
        `How do you propose we distribute the responsibilities for the ${e2}?`
      ];
      const dFrames = [
        `I would love to help you organize the ${e2} so everything stays neat.`,
        `Whenever we practice with the ${desc} ${e1}, our team communicates much better.`,
        `I can take the initiative to ${act} the ${e1} if that helps you.`,
        `By coordinating our approach to the ${e1}, we ensure that the ${e2} is handled properly.`,
        `Our group has developed a very constructive rhythm for solving problems together.`,
        `I appreciate your thoughtful suggestions regarding the management of the ${desc} ${e1}.`,
        `Taking a structured approach prevents unexpected complications from arising later.`,
        `We have noticed a substantial improvement in our fluency since we started practicing.`,
        `Cooperation allows us to accomplish complex tasks with minimal friction.`,
        `Maintaining clear communication keeps everyone aligned on our shared objectives.`,
        `We find it rewarding to explore challenging dialogue scenarios as a team.`,
        `Systematic preparation enables us to deliver articulate responses with confidence.`,
        `Our team consistently demonstrates outstanding dedication during daily exercises.`
      ];
      const sFrames = [
        `Let us make sure we understand each step before we ${act} together.`,
        `Refining our technique with the ${desc} ${e1} significantly accelerates our team's progress.`,
        `I will summarize our main takeaways regarding the ${e2} for the group.`,
        `Consistently applying these techniques ensures our speech remains polished.`,
        `We should establish clear benchmarks to monitor our communicative development.`,
        `Effective turn-taking allows every participant to express their viewpoint fully.`,
        `We welcome constructive feedback because it helps us refine our articulation.`,
        `Balancing precision with spontaneous expression is key to conversational agility.`,
        `Our collective enthusiasm makes mastering new vocabulary an enjoyable process.`,
        `Let us maintain this positive momentum throughout the remainder of the week.`,
        `We are well prepared to engage in spontaneous discussions on diverse topics.`,
        `Dedication to daily practice transforms theoretical knowledge into active skill.`,
        `Every completed session deepens our appreciation for nuanced language use.`,
        `We take genuine pride in our ability to communicate clearly and courteously.`
      ];
      items = [
        qFrames[(d * 7) % qFrames.length],
        dFrames[(d * 5) % dFrames.length],
        sFrames[(d * 3) % sFrames.length]
      ];
    } else {
      // Advanced
      const qFrames = [
        `If we finish preparing the ${e1} early, could we practice the ${e2} as well?`,
        `Would you mind showing me the most efficient technique to handle the ${desc} ${e1}?`,
        `Could we deliberate on the best way to ${act} the ${e2} under current conditions?`,
        `How might we adapt our strategy so that the ${e1} seamlessly supports our collective goals?`,
        `To what degree does our execution with the ${desc} ${e1} influence our overall evaluation?`,
        `What contingency measures should we implement in case the ${e2} requires modification?`,
        `Can we evaluate the relative advantages of differing perspectives on the ${e1}?`,
        `How can we best synthesize our individual contributions regarding the ${desc} ${e2}?`,
        `Would it be prudent to conduct a preliminary trial before we ${act} publicly?`,
        `What criteria should we prioritize when assessing the impact of the ${e1}?`,
        `Is there an opportunity to enhance our delivery by incorporating the ${desc} ${e2}?`,
        `How effectively does our approach to ${act} align with professional standards?`
      ];
      const dFrames = [
        `I noticed that whenever we ${act} cooperatively, our entire team accomplishes much more.`,
        `Refining our technique with the ${desc} ${e1} significantly accelerates our team's progress.`,
        `I appreciate your thoughtful perspective on how the ${e1} contributes to our overall success.`,
        `Demonstrating genuine fluency requires us to ${act} the ${desc} ${e1} with complete confidence.`,
        `A thorough analysis reveals that consistent verbal rehearsal dramatically improves retention.`,
        `Our ability to navigate unexpected conversational turns reflects disciplined preparation.`,
        `Collaborative synergy enables us to tackle intricate topics with remarkable poise.`,
        `We have established a sophisticated standard for articulating complex arguments clearly.`,
        `Synthesizing diverse viewpoints enriches our collective understanding of the ${desc} ${e1}.`,
        `Our articulate discourse reflects an advanced command of idiomatic and syntactic nuance.`,
        `We consistently apply analytical rigor to refine our pronunciation and cadence.`,
        `Maintaining composed articulation under time constraints demonstrates authentic mastery.`,
        `Our shared commitment to communicative excellence is evident in every exchange.`
      ];
      const sFrames = [
        `In order to optimize our execution with the ${e1}, we should carefully evaluate the ${e2}.`,
        `Demonstrating genuine fluency requires us to ${act} the ${desc} ${e1} with complete confidence.`,
        `I recommend we consolidate our observations on the ${e1} into a cohesive summary.`,
        `Cultivating linguistic versatility empowers us to communicate persuasively in any setting.`,
        `We must balance technical precision with natural conversational flow at all times.`,
        `Engaging in structured debate cultivates both critical reasoning and rhetorical agility.`,
        `Our deliberate focus on expressive cadence elevates the impact of our spoken words.`,
        `We take full ownership of our linguistic development and celebrate continuous growth.`,
        `Mastering complex grammatical structures unlocks sophisticated avenues of self-expression.`,
        `Let us channel our insights into a compelling and articulate concluding statement.`,
        `The depth of our preparation allows us to articulate spontaneous thoughts with ease.`,
        `Every conversation serves as a masterclass in diplomacy, empathy, and eloquence.`,
        `We approach advanced linguistic challenges with intellectual curiosity and vigor.`,
        `True mastery is demonstrated when sophisticated concepts are communicated effortlessly.`
      ];
      items = [
        qFrames[(d * 7) % qFrames.length],
        dFrames[(d * 5) % dFrames.length],
        sFrames[(d * 3) % sFrames.length]
      ];
    }
  }

  // ==========================================================================
  // 3. AGE BRACKET: 10-12 (CONCEPTUAL VOCABULARY, IDIOMS, REASONING)
  // ==========================================================================
  else if (ageGroup === '10-12') {
    const d = normalizedDay;
    const e = lexicon.entities[(d * 7) % lexicon.entities.length];
    const idiom = lexicon.idioms[(d * 5) % lexicon.idioms.length];
    const desc = lexicon.descriptors[(d * 3) % lexicon.descriptors.length];
    const ctx = lexicon.situationalContexts[(d * 2) % lexicon.situationalContexts.length];

    if (level === 'Beginner') {
      const frames1 = [
        `Practicing with ${e} is important because it strengthens our daily communication habits.`,
        `Demonstrating patience with ${e} allows us to overcome difficulties ${ctx}.`,
        `Mastering the nuances of ${e} is an essential milestone in building true conversational fluency.`,
        `When we prioritize clear thinking around ${e}, our verbal explanations become much sharper.`,
        `Developing a structured routine for ${e} ensures that no critical details are overlooked.`,
        `Understanding why ${e} matters gives us greater motivation during our practice sessions.`,
        `We can observe how effective coordination regarding ${e} prevents unnecessary confusion.`,
        `Taking time to examine the core components of ${e} solidifies our overall understanding.`,
        `A grounded perspective on ${e} enables us to contribute meaningfully to group discussions.`,
        `Learning how to speak articulately about ${e} builds lasting self-confidence in school.`,
        `Consistent reflection upon ${e} transforms abstract ideas into practical communication skills.`,
        `We recognize that disciplined attention to ${e} pays significant dividends in the long run.`
      ];
      const frames2 = [
        `We should ensure that everyone contributes equitably when we work ${ctx}.`,
        `I believe that a ${desc} perspective helps us resolve misunderstandings quickly.`,
        `When we maintain open communication ${ctx}, our collective problem-solving becomes much more ${desc}.`,
        `Adopting a ${desc} approach encourages all participants to voice their insights freely.`,
        `Our shared dedication to maintaining ${desc} standards elevates the entire group's performance.`,
        `Clear and empathetic dialogue ${ctx} fosters an environment of mutual trust and respect.`,
        `We strive to approach unfamiliar challenges ${ctx} with curiosity and a ${desc} mindset.`,
        `Listening carefully to differing viewpoints ${ctx} sharpens our own reasoning abilities.`,
        `A ${desc} attitude allows us to navigate constructive disagreements without hostility.`,
        `Collaborative teamwork ${ctx} is most productive when grounded in ${desc} principles.`,
        `We find that intentional cooperation ${ctx} consistently produces superior outcomes.`,
        `Practicing disciplined composure ${ctx} reinforces both maturity and eloquence.`,
        `Every interaction ${ctx} provides an authentic venue to apply our communication skills.`
      ];
      const frames3 = [
        `Could you elaborate on the primary reasons why this approach is considered ${desc}?`,
        `Why is it particularly beneficial to focus on ${e} during our collaborative sessions?`,
        `Could you share your insights on how ${e} influences our ongoing team dynamics?`,
        `What evidence supports the assertion that this methodology produces the best results?`,
        `How might we objectively assess whether our strategy regarding ${e} is truly effective?`,
        `What specific advantages arise when we integrate ${e} into our daily routine?`,
        `Can you clarify the key distinction between these two perspectives on ${e}?`,
        `How can we refine our verbal delivery to ensure our arguments are compelling and clear?`,
        `What constructive alternatives would you propose to enhance our current plan?`,
        `In what ways does mastering ${e} prepare us for future academic challenges?`,
        `Could you outline the logical progression that led to your conclusion about ${e}?`,
        `How do our communicative habits influence the way others perceive our ideas?`,
        `What valuable lessons have we gathered from analyzing this scenario together?`,
        `How can we best apply these communication principles outside of the classroom?`
      ];
      items = [
        frames1[(d * 7) % frames1.length],
        frames2[(d * 5) % frames2.length],
        frames3[(d * 3) % frames3.length]
      ];
    } else if (level === 'Intermediate') {
      const frames1 = [
        `In order to ${idiom}, we should systematically organize our approach to the ${e}.`,
        `Learning to ${idiom} requires consistent practice and a willingness to adapt ${ctx}.`,
        `By actively choosing to ${idiom}, we navigate the subtle complexities of ${e} with maturity.`,
        `Whenever our team decides to ${idiom}, our collaborative efficiency visibly increases.`,
        `The discipline required to ${idiom} directly correlates with our communicative success.`,
        `Recognizing the strategic moment to ${idiom} distinguishes proactive problem solvers.`,
        `We encourage one another to ${idiom} rather than succumbing to hasty assumptions.`,
        `A commitment to ${idiom} ensures that our dialogue remains objective and focused.`,
        `Understanding how to ${idiom} enables us to mediate conflicting opinions diplomatically.`,
        `Cultivating the capability to ${idiom} prepares us for increasingly demanding scenarios.`,
        `When leaders learn to ${idiom}, they foster genuine cohesion throughout the entire team.`,
        `Our ongoing effort to ${idiom} serves as a powerful catalyst for personal growth.`
      ];
      const frames2 = [
        `I believe that maintaining a ${desc} attitude allows us to resolve misunderstandings ${ctx}.`,
        `The correlation between disciplined preparation of ${e} and ${desc} outcomes is undeniable.`,
        `A thorough examination of ${e} demonstrates why maintaining a ${desc} approach is indispensable ${ctx}.`,
        `Adopting a ${desc} framework allows us to evaluate competing hypotheses rigorously.`,
        `Our collective ability to articulate ${desc} arguments elevates the standard of discussion.`,
        `Demonstrating a ${desc} disposition ${ctx} prevents minor disputes from escalating.`,
        `We find that systematic analysis of ${e} yields profoundly ${desc} insights for the group.`,
        `A well reasoned and ${desc} response consistently commands attention and respect.`,
        `Prioritizing ${desc} communication principles establishes a benchmark of integrity.`,
        `The integration of empirical facts with a ${desc} presentation strengthens our credibility.`,
        `Sustaining a ${desc} dialogue ${ctx} proves our capacity for mature intellectual engagement.`,
        `We appreciate how a ${desc} methodology simplifies complex problem-solving.`,
        `Every member benefits when our discussions are characterized by ${desc} rigor.`
      ];
      const frames3 = [
        `What evidence supports the conclusion that handling ${e} this way yields the best outcome?`,
        `How can we cultivate an environment where everyone feels empowered to discuss ${e}?`,
        `What constructive feedback would you offer to refine our handling of this situation?`,
        `How might we substantiate our claims regarding ${e} with verified empirical evidence?`,
        `To what extent do situational variables ${ctx} alter the optimal course of action?`,
        `What underlying factors might explain the differing opinions surrounding ${e}?`,
        `How can we balance analytical thoroughness with concise conversational delivery?`,
        `What potential challenges might arise if we fail to implement these recommendations?`,
        `Could you identify the pivotal assumption upon which this reasoning is based?`,
        `How do ethical considerations inform our decisions when dealing with ${e}?`,
        `What strategic adjustments should we make to optimize our collective workflow?`,
        `In what manner does our communicative posture influence the reception of our proposals?`,
        `How can we synthesize diverse perspectives to build a unified consensus?`,
        `What long-term advantages stem from mastering this level of conversational precision?`
      ];
      items = [
        frames1[(d * 7) % frames1.length],
        frames2[(d * 5) % frames2.length],
        frames3[(d * 3) % frames3.length]
      ];
    } else {
      // Advanced
      const frames1 = [
        `Navigating complex interactions ${ctx} requires both emotional intelligence and pragmatic reasoning.`,
        `Strategic mastery of ${e} demands that we synthesize empirical insights with intuitive judgment ${ctx}.`,
        `Articulating a coherent philosophy regarding ${e} elevates our discourse to an advanced conceptual level.`,
        `A sophisticated deconstruction of ${e} exposes the underlying systemic patterns that govern behavior.`,
        `The ability to evaluate ${e} objectively amidst ambiguity is the definitive hallmark of critical acumen.`,
        `Refining our analytical vocabulary regarding ${e} empowers us to express nuanced deductions with precision.`,
        `Rigorous intellectual engagement with ${e} necessitates moving beyond superficial impressions.`,
        `The synthesis of theoretical principles and practical application regarding ${e} yields profound results.`,
        `We must critically examine whether prevailing assumptions regarding ${e} remain valid under scrutiny.`,
        `Formulating a rigorous conceptual model for ${e} facilitates proactive problem resolution.`,
        `The dialectic exploration of ${e} illuminates subtle nuances that are frequently overlooked.`,
        `Demonstrating intellectual maturity entails interrogating our own preconceptions concerning ${e}.`
      ];
      const frames2 = [
        `By learning how to ${idiom}, we avoid unnecessary friction and cultivate genuine mutual respect.`,
        `Recognizing when to ${idiom} empowers our group to transcend conventional dialogue barriers.`,
        `The ability to ${idiom} under demanding circumstances reflects profound emotional resilience ${ctx}.`,
        `When participants collectively ${idiom}, collaborative synergy reaches its fullest potential.`,
        `Mastering the art to ${idiom} allows us to navigate diplomatic impasses with consummate skill.`,
        `Our determination to ${idiom} reinforces a culture of mutual accountability and excellence.`,
        `Knowing precisely how to ${idiom} enables communicators to resolve complex disputes peacefully.`,
        `The deliberate decision to ${idiom} demonstrates advanced situational awareness ${ctx}.`,
        `Those who master the capacity to ${idiom} consistently inspire confidence and consensus.`,
        `By striving to ${idiom}, we transform potentially divisive disagreements into collaborative triumphs.`,
        `An instinctive grasp of when to ${idiom} distinguishes truly exceptional communicative leaders.`,
        `The habitual practice to ${idiom} ensures that our collaborative momentum remains uncompromised.`,
        `Cultivating the discipline to ${idiom} remains one of our most formidable rhetorical assets.`
      ];
      const frames3 = [
        `I would argue that the subtle nuances of ${e} play a decisive role in shaping our perspective.`,
        `To what degree does our collective interpretation of ${desc} principles dictate our response to ${e}?`,
        `How might we rigorously substantiate our deductions concerning the long-term impact of ${desc} methodologies?`,
        `What profound implications emerge when we subject the conventional doctrine of ${e} to critical analysis?`,
        `How can we reconcile the dialectic tension between theoretical elegance and practical viability ${ctx}?`,
        `To what extent does language itself constrain or expand our capacity to conceptualize ${e}?`,
        `What criteria determine whether an argumentative synthesis regarding ${e} is genuinely robust?`,
        `How do subtle shifts in communicative framing alter stakeholder perceptions ${ctx}?`,
        `In what manner does empirical verification fortify our rhetorical credibility during debate?`,
        `What systemic vulnerabilities might arise if our foundational premises regarding ${e} are flawed?`,
        `How can we cultivate rhetorical agility without sacrificing philosophical depth or authenticity?`,
        `What cognitive mechanisms enable proficient thinkers to synthesize disparate viewpoints effortlessly?`,
        `How does disciplined verbal articulation serve as an engine for accelerated intellectual discovery?`,
        `Ultimately, the measure of communicative eloquence lies in its power to enlighten, persuade, and inspire.`
      ];
      items = [
        frames1[(d * 7) % frames1.length],
        frames2[(d * 5) % frames2.length],
        frames3[(d * 3) % frames3.length]
      ];
    }
  }

  // ==========================================================================
  // 4. AGE BRACKET: 13-16 (ACADEMIC ARTICULATION, FORMAL DISCOURSE, AGILITY)
  // ==========================================================================
  else {
    const d = normalizedDay;
    const e = lexicon.entities[(d * 7) % lexicon.entities.length];
    const theme = lexicon.academicThemes[(d * 5) % lexicon.academicThemes.length];
    const desc = lexicon.descriptors[(d * 3) % lexicon.descriptors.length];
    const ctx = lexicon.situationalContexts[(d * 2) % lexicon.situationalContexts.length];

    if (level === 'Beginner') {
      const frames1 = [
        `Establishing a coherent strategy regarding ${e} noticeably improves collaborative productivity.`,
        `A structured examination of ${e} illustrates how systematic preparation yields ${desc} dividends.`,
        `Systematically integrating ${theme} into our daily routine reinforces foundational academic discipline.`,
        `An objective evaluation of ${e} demonstrates the tangible value of structured methodological rigor.`,
        `Engaging in disciplined inquiry surrounding ${e} cultivates heightened analytical precision.`,
        `Developing a robust communicative framework for ${e} enables articulate participation in academic seminars.`,
        `The deliberate synthesis of ${e} and core conceptual principles enhances overall intellectual retention.`,
        `Careful scrutiny of the mechanisms underlying ${e} reveals profound structural insights.`,
        `Formulating clear, declarative assertions regarding ${e} prevents rhetorical ambiguity.`,
        `A thorough academic review of ${e} provides the prerequisite foundation for subsequent advanced research.`,
        `Sustained concentration upon ${e} fosters both conceptual clarity and verbal sophistication.`,
        `We must articulate our observations regarding ${e} with measured cadence and uncompromising precision.`
      ];
      const frames2 = [
        `How might we objectively analyze the influence of ${theme} in our immediate environment?`,
        `What empirical criteria should we establish to evaluate the efficacy of ${theme} ${ctx}?`,
        `In what manner does our communicative approach to ${e} reflect broader organizational principles?`,
        `To what degree does our comprehension of ${theme} inform our strategic decision-making?`,
        `What methodologies are best suited to quantify the pedagogical benefits of ${theme}?`,
        `How do contemporary scholars categorize the intersection between ${e} and ${theme}?`,
        `What theoretical challenges arise when applying ${theme} to complex empirical scenarios?`,
        `In what capacity does an understanding of ${theme} enhance our collaborative problem-solving capabilities?`,
        `How might we delineate the precise boundaries between empirical evidence and theoretical extrapolation in ${theme}?`,
        `What primary variables must be isolated when investigating the systemic ramifications of ${theme}?`,
        `How can we construct an evidentiary framework to corroborate our findings regarding ${theme}?`,
        `To what extent do historical precedents illuminate our current analysis of ${theme}?`,
        `What diagnostic benchmarks should we institute to verify the validity of our deductions in ${theme}?`
      ];
      const frames3 = [
        `It is advantageous to maintain open dialogue ${ctx} to preclude potential ambiguities.`,
        `Engaging in deliberate discourse regarding ${e} cultivates heightened analytical precision.`,
        `Maintaining an articulate and ${desc} posture ${ctx} facilitates seamless multilateral consensus.`,
        `Structured verbal articulation reinforces the cognitive pathways responsible for analytical reasoning.`,
        `Proactive communicative engagement ensures that disparate perspectives are harmonized constructively.`,
        `Cultivating oratorical poise under academic scrutiny is an invaluable asset for collegiate advancement.`,
        `The disciplined application of ${desc} principles elevates the standard of classroom discourse.`,
        `Adhering to rigorous standards of clarity preserves the integrity of collaborative academic investigations.`,
        `A commitment to intellectual candor ${ctx} stimulates profound insights and mutual respect.`,
        `Mastering the art of measured rhetorical delivery empowers students to advocate persuasively.`,
        `Deliberate oral rehearsal transforms abstract academic theories into accessible, persuasive arguments.`,
        `Consistency in formal communication reflects intellectual maturity, self-regulation, and scholarly discipline.`,
        `Every seminar exchange provides a vital crucible for refining our argumentation and oratorical eloquence.`,
        `Ultimately, academic articulation is not merely decorative; it is the fundamental engine of intellectual discovery.`
      ];
      items = [
        frames1[(d * 7) % frames1.length],
        frames2[(d * 5) % frames2.length],
        frames3[(d * 3) % frames3.length]
      ];
    } else if (level === 'Intermediate') {
      const frames1 = [
        `An articulate examination of ${e} reveals profound interconnections with broader ${theme}.`,
        `Interrogating the foundational assumptions surrounding ${e} exposes critical nuances within ${theme}.`,
        `A sophisticated deconstruction of ${e} underscores the imperative for rigorous conceptual coherence.`,
        `The dialectical interplay between ${e} and ${theme} highlights the necessity of multi-disciplinary synthesis.`,
        `Subjecting the structural dynamics of ${e} to rigorous critique uncovers latent systemic complexities.`,
        `A nuanced appraisal of ${e} demonstrates how theoretical paradigms actively configure empirical observation.`,
        `Formulating an analytical thesis on ${e} requires isolating underlying variables from incidental phenomena.`,
        `The methodological evaluation of ${e} provides an authoritative foundation for comparative analysis.`,
        `Investigating the historical evolution of ${e} contextualizes contemporary theoretical debates within ${theme}.`,
        `An intellectually honest critique of ${e} must address both its empirical strengths and epistemic limitations.`,
        `Deconstructing the rhetorical devices employed to defend ${e} reveals subtle ideological assumptions.`,
        `Synthesizing disparate scholarly interpretations of ${e} deepens our holistic comprehension of ${theme}.`
      ];
      const frames2 = [
        `Cultivating a ${desc} methodology ${ctx} reinforces both analytical rigor and ethical integrity.`,
        `The synthesis of ${desc} inquiry and pragmatic execution ${ctx} establishes an exemplary benchmark.`,
        `The pragmatic integration of ${theme} ${ctx} demonstrates remarkable communicative adaptability and maturity.`,
        `Adopting a ${desc} pedagogical framework enables researchers to navigate paradigm shifts effortlessly.`,
        `Maintaining a ${desc} intellectual temperament ${ctx} safeguards against dogmatic cognitive inertia.`,
        `The deliberate implementation of ${desc} investigative protocols fortifies our empirical credibility.`,
        `Demonstrating a ${desc} posture during high-stakes academic discourse preserves professional decorum.`,
        `Our shared dedication to ${desc} analytical inquiry fosters an intellectually invigorating atmosphere.`,
        `Applying a ${desc} hermeneutic to controversial texts facilitates balanced and objective analysis.`,
        `The convergence of ${desc} scholarship and ethical advocacy produces transformative societal insights.`,
        `Cultivating a ${desc} communicative standard ${ctx} ensures that debate remains intellectually rigorous.`,
        `A thoroughly ${desc} orientation toward scholarship inspires innovative conceptual breakthroughs.`,
        `Every rigorous inquiry conducted ${ctx} exemplifies the transformative power of ${desc} methodology.`
      ];
      const frames3 = [
        `To what extent does our collective perception of ${e} dictate our subsequent communicative decisions?`,
        `How might we reconcile disparate perspectives regarding ${e} without compromising intellectual honesty?`,
        `What overarching implications emerge when we subject the tenets of ${desc} discourse to critical scrutiny?`,
        `How do contemporary epistemic frameworks influence the interpretation of empirical data regarding ${e}?`,
        `What criteria must be satisfied to validate a novel theoretical paradigm within ${theme}?`,
        `To what degree does the semantic ambiguity of ${e} complicate multilateral scholarly consensus?`,
        `How can researchers counteract unconscious cognitive biases when analyzing complex phenomena ${ctx}?`,
        `What structural impediments hinder the seamless translation of theoretical models into empirical practice?`,
        `How does the rigorous interrogation of first principles catalyze paradigm shifts within academia?`,
        `What ethical imperatives must govern the dissemination of scientific and sociological research today?`,
        `How might we construct a versatile analytical rubric capable of evaluating competing claims regarding ${e}?`,
        `In what manner does interdisciplinary collaboration challenge the insular orthodoxies of specialized fields?`,
        `What intellectual virtues are essential to sustain productive discourse amidst deep ideological divisions?`,
        `Ultimately, how does the pursuit of conceptual clarity elevate our collective capacity for human understanding?`
      ];
      items = [
        frames1[(d * 7) % frames1.length],
        frames2[(d * 5) % frames2.length],
        frames3[(d * 3) % frames3.length]
      ];
    } else {
      // Advanced
      const frames1 = [
        `Rigorous engagement with ${e} necessitates a nuanced synthesis of empirical observation and conceptual synthesis.`,
        `Epistemological rigor regarding ${e} compels us to scrutinize how contextual paradigms inform communicative efficacy.`,
        `An exhaustive treatise on ${e} demonstrates that rhetorical agility is inextricably bound to conceptual precision.`,
        `The dialectical synthesis of ${e} and ${theme} redefines the boundaries of contemporary academic discourse.`,
        `Interrogating the ontological foundations of ${e} exposes the implicit normative structures embedded within ${theme}.`,
        `A comprehensive theoretical deconstruction of ${e} illustrates the limits of reductionist empiricism.`,
        `Formulating an advanced critique of ${e} requires navigating the intricate nexus of rhetoric, logic, and semiotics.`,
        `The intellectual potency of our discourse regarding ${e} directly corresponds to our willingness to confront paradox.`,
        `Synthesizing disparate scholarly frameworks regarding ${e} catalyzes profound theoretical innovation.`,
        `An exhaustive inquiry into ${e} reveals how discursive conventions both constrain and empower human agency.`,
        `The sophisticated appraisal of ${e} transcends superficial dualisms, fostering multidimensional insight.`,
        `True scholarly mastery is demonstrated when the most intricate dynamics of ${e} are articulated with effortless clarity.`
      ];
      const frames2 = [
        `The intersection of ${theme} and ${desc} communicative strategies fundamentally redefines contextual discourse ${ctx}.`,
        `The convergence of ${desc} rhetoric and ${theme} establishes an authoritative framework for collaborative diplomacy ${ctx}.`,
        `Transcending conventional discourse ${ctx} requires a deliberate mastery of both ${theme} and ${desc} dialectics.`,
        `The integration of ${theme} into high-stakes negotiations provides an impregnable bulwark against sophistry.`,
        `Applying ${desc} dialectical techniques ${ctx} empowers scholars to deconstruct fallacious presuppositions with surgical precision.`,
        `A profound comprehension of ${theme} enables oratorical agility across diverse academic and professional arenas.`,
        `The synthesis of ${theme} and ethical jurisprudence establishes an enduring benchmark for scholarly integrity.`,
        `Mastering the subtleties of ${theme} ${ctx} facilitates the seamless reconciliation of competing epistemological models.`,
        `Deploying ${desc} communicative paradigms elevates standard debate into transformative philosophical dialogue.`,
        `The authoritative command of ${theme} distinguishes genuine thought leaders from mere academic technicians.`,
        `Harmonizing ${desc} rhetoric with rigorous empirical verification produces undeniably compelling scholarship.`,
        `The scholarly pursuit of ${theme} ${ctx} demands an unwavering commitment to intellectual honesty and rigor.`,
        `Cultivating ${desc} communicative mastery remains the quintessential hallmark of modern intellectual leadership.`
      ];
      const frames3 = [
        `Perhaps the most compelling argument for refining our discourse surrounding ${e} lies in its capacity to cultivate intellectual agility.`,
        `To what degree does the dialectic tension inherent in ${e} stimulate innovative cognitive breakthroughs?`,
        `Ultimately, the hallmark of mature articulation is the capacity to interrogate the systemic architecture of ${e} with unflinching clarity.`,
        `What profound transformations occur within our cognitive architecture when we master advanced rhetorical agility?`,
        `How does the relentless pursuit of conceptual precision liberate scholarship from the shackles of dogmatism?`,
        `In what manner does the sophisticated articulation of ${e} serve as an indispensable catalyst for human progress?`,
        `How might we synthesize empirical rigor and poetic resonance to forge an undeniably persuasive mode of discourse?`,
        `What enduring legacy is forged when an academic community commits itself wholeheartedly to communicative excellence?`,
        `How do the foundational tenets of critical inquiry empower future generations to interrogate established paradigms?`,
        `In what ways does the mastery of spoken rhetoric deepen our capacity for profound intellectual and emotional empathy?`,
        `How can the synthesis of rigorous logic and articulate speech illuminate the most intractable paradoxes of our time?`,
        `What transformative horizon emerges when communicative mastery is deployed in service of universal truth and wisdom?`,
        `Ultimately, authentic eloquence is the sublime union of profound thought, disciplined speech, and ethical conviction.`,
        `By dedicating ourselves to the art of articulate speech, we honor the highest aspirations of human intellect and dialogue.`
      ];
      items = [
        frames1[(d * 7) % frames1.length],
        frames2[(d * 5) % frames2.length],
        frames3[(d * 3) % frames3.length]
      ];
    }
  }

  const phoneticHint = lexicon.phonetic || `/${String(topicId).replace(/-/g, ' ')}/`;

  return {
    id: cardId,
    categoryId: catNum,
    topicId: topicId,
    day: normalizedDay,
    ageGroup,
    level,
    practiceItems: items,
    phoneticHint,
  };
}

export { getCardPracticeData } from './conversationalCurriculum';
