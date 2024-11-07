from flask import Flask, render_template

app = Flask(__name__)


team_members = [
    {
        'name': 'Lim Qian Yun',
        'department': 'Top Committee',
        'role': 'Project Director',
        'image': 'qianyun.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/johndoe',
            'facebook': 'https://facebook.com/johndoe',
            'linkedin': 'https://linkedin.com/in/johndoe'
        }
    },
    {
        'name': 'Wong Wei Ze',
        'department': 'Top Committee',
        'role': 'Vice Project Director',
        'image': '2.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },
    {
        'name': 'Lingges A/L Muniandy',
        'department': 'Top Committee',
        'role': 'Vice Project Director',
        'image': '3.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },
    {
        'name': 'Siti Maisarah Binti Khairul Anwar',
        'department': 'Top Committee',
        'role': 'Secretary',
        'image': '4.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },
    {
        'name': 'Chew Jum Liang',
        'department': 'Top Committee',
        'role': 'Treasurer',
        'image': '5.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },
    {
        'name': 'Tan Wei Yi',
        'department': 'Programme',
        'role': 'Head Executive',
        'image': '6.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },
    {
        'name': 'Ng Qiu Jun',
        'department': 'Programme',
        'role': 'Vice Executive',
        'image': '7.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },{
        'name': 'Padma Pireeya A/P S Soundra Rajan',
        'department': 'Programme',
        'role': 'Vice Executive',
        'image': '8.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },
    {
        'name': 'Asreena Chulaphong A/P Akhom',
        'department': 'Programme',
        'role': 'Coordinator',
        'image': '9.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },
    {
        'name': 'Reeyeankha',
        'department': 'Programme',
        'role': 'Coordinator',
        'image': '10.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },
    {
        'name': 'Muhammad Ammar Danial Bin Abdullah',
        'department': 'Programme',
        'role': 'Coordinator',
        'image': '11.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },
    
    {
        'name': 'Ashman Bin Mohd Fauzi',
        'department': 'Programme',
        'role': 'Coordinator',
        'image': '12.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },
    {
        'name': 'Ahmad Asyraf Bin Ahmad Johari',
        'department': 'Programme',
        'role': 'Coordinator',
        'image': '13.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },
    {
        'name': 'Shereen Ilyza Binti Sheik Mujibu Rahman ',
        'department': 'Public Relations and Documentation',
        'role': 'Head Executive',
        'image': '14.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },
    {
        'name': 'Ching Ke Chee',
        'department': 'Public Relations and Documentation',
        'role': 'Vice Executive',
        'image': '15.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },
    {
        'name': 'Law Zhe Yin',
        'department': 'Public Relations and Documentation',
        'role': 'Vice Executive',
        'image': '16.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },
    {
        'name': 'Muhammad Faiq Fadhlullah',
        'department': 'Public Relations and Documentation',
        'role': 'Coordinator',
        'image': '17.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },
    {
        'name': 'Thaneshwaran A/L Sarsidharan',
        'department': 'Public Relations and Documentation',
        'role': 'Coordinator',
        'image': '18.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },
    {
        'name': 'Nur Nadia Nabila Binti Mohamad Fauzi',
        'department': 'Public Relations and Documentation',
        'role': 'Coordinator',
        'image': '19.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },
    {
        'name': 'Airiel Hazim Bin Redzuan Ng',
        'department': 'Public Relations and Documentation',
        'role': 'Coordinator',
        'image': '20.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },
    {
        'name': 'Khairin Aimi Binti Mohd Ashri',
        'department': 'Publicity and Marketing',
        'role': 'Had Executive',
        'image': '21.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },
    {
        'name': 'Danial Hakim Bin Kamal Azwa',
        'department': 'Publicity and Marketing',
        'role': 'Vice Executive',
        'image': '22.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },
    {
        'name': 'Lee Zhi Syeh',
        'department': 'Publicity and Marketinga',
        'role': 'Vice Executive',
        'image': '23.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },
    {
        'name': 'Raziqin Husna Binti Abdul Wahid',
        'department': 'Publicity and Marketing',
        'role': 'Coordinator',
        'image': '24.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },
    {
        'name': 'Adam Zafry Bin Zaharin',
        'department': 'Publicity and Marketing',
        'role': 'Coordinator',
        'image': '25.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },
    {
        'name': 'Chung Piek Hui',
        'department': 'Publicity and Marketing',
        'role': 'Coordinator',
        'image': '26.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },
    {
        'name': 'Arwen Laung Ai Wen',
        'department': 'Publicity and Marketing',
        'role': 'Coordinator',
        'image': '27.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },
    {
        'name': 'Goh Shu Ying',
        'department': 'Publicity and Marketing',
        'role': 'Coordinator',
        'image': '28.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },
    {
        'name': 'Muhammad Aqif Wafiy Bin Mohd Farid',
        'department': 'Sponsorship',
        'role': 'Head Executive',
        'image': '29.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },
    {
        'name': 'Chin Yu Yuan',
        'department': 'Sponsorship',
        'role': 'Vice Executive',
        'image': '30.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },
    {
        'name': 'Mervyn Chew Yew Zhang',
        'department': 'Sponsorship',
        'role': ' Vice Executive',
        'image': '31.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },
    {
        'name': 'Woo Pei Wen',
        'department': 'Sponsorship',
        'role': 'Coordinator',
        'image': '32.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },
    {
        'name': 'Sabrina Binti Sofian',
        'department': 'Sponsorship',
        'role': 'Coordinator',
        'image': '33.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },
    {
        'name': 'Yeoh Hao Jing',
        'department': 'Sponsorship',
        'role': 'Coordinator',
        'image': '34.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },{
        'name': 'Shirley Binti Osman',
        'department': 'Sponsorship',
        'role': 'Coordinator',
        'image': '35.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },
    {
        'name': 'Hemwaren A/L Kunalan',
        'department': 'Logistics',
        'role': 'Head Executive',
        'image': '36.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },
    {
        'name': 'Tan Jun Cheng',
        'department': 'Logistics',
        'role': 'Vice Executive',
        'image': '37.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },{
        'name': 'Ooi Seong Kin',
        'department': 'Logistics',
        'role': 'Vice Executive',
        'image': '38.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },
    {
        'name': 'Yeoh Shu Yi',
        'department': 'Logistics',
        'role': 'Coordinator',
        'image': '39.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },
    {
        'name': 'Wan Muhammad Adam Bin Wan Mohd Fauzi',
        'department': 'Logistics',
        'role': 'Coordinator',
        'image': '40.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },
    {
        'name': 'Ng Yin Thong',
        'department': 'Logistics',
        'role': 'Coordinator',
        'image': '41.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },
    {
        'name': 'Tan Tse Han',
        'department': 'Logistics',
        'role': 'Coordinator',
        'image': '42.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },
    {
        'name': 'Shivabala A/L Ganeish',
        'department': 'Logistics',
        'role': 'Coordinator',
        'image': '43.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },
    {
        'name': 'Loo Chi Hao',
        'department': 'Technical',
        'role': 'Head Executive',
        'image': '44.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },
    {
        'name': 'Koay Chun Keat',
        'department': 'Technical',
        'role': 'Vice Executive',
        'image': '45.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },
    {
        'name': 'Lim Wen Hao',
        'department': 'Technical',
        'role': 'Vice Executive',
        'image': '46.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },
    {
        'name': 'Liew Choy Yein',
        'department': 'Technical',
        'role': 'Coordinator',
        'image': '47.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },
    {
        'name': 'Cheng Chea Hao',
        'department': 'Technical',
        'role': 'Coordinator',
        'image': '48.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },
    {
        'name': 'Lim Miin Ning',
        'department': 'Technical',
        'role': 'Coordinator',
        'image': '49.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },
    {
        'name': 'Har Tien Yu',
        'department': 'Technical',
        'role': 'Coordinator',
        'image': '50.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },
    {
        'name': 'Andyclos A/L Boon Mee',
        'department': 'Technical',
        'role': 'Coordinator',
        'image': '51.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },
    {
        'name': 'Bernadatte Lee Pei Chen',
        'department': 'Design & Multimedia',
        'role': 'Head Executive',
        'image': '52.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },
    {
        'name': 'Khoo Iu Wan',
        'department': 'Design and Multimedia',
        'role': 'Vice Executive',
        'image': '53.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },
    {
        'name': 'Hazim Muhsin Bin Munir',
        'department': 'Design and Multimedia',
        'role': 'Vice Executive',
        'image': '54.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },
    {
        'name': 'Najihah Hanani Binti Ahmad Farid',
        'department': 'Design and Multimedia',
        'role': 'Coordinator',
        'image': '55.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },
    {
        'name': 'Sergio Law Zhe Xian',
        'department': 'Design and Multimedia',
        'role': 'Coordinator',
        'image': '56.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },
    {
        'name': 'Darren Fu Hon Meng',
        'department': 'Design and Multimedia',
        'role': 'Coordinator',
        'image': '57.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },
    {
        'name': 'Gordon Chai Ming Xun',
        'department': 'Design and Multimedia',
        'role': 'Coordinator',
        'image': '58.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },
    {
        'name': 'Hadrie Hakimi Bin Nazarudin',
        'department': 'Design and Multimedia',
        'role': 'Coordinator',
        'image': '59.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },
    {
        'name': 'Loh Yi Han',
        'department': 'Design and Multimedia',
        'role': 'Coordinator',
        'image': '60.jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    },
    {
        'name': 'Wong Mei Zhen',
        'department': 'Design and Multimedia',
        'role': 'Coordinator',
        'image': '61 (1).jpg',
        'social_links': {
            'instagram': 'https://instagram.com/janesmith',
            'facebook': 'https://facebook.com/janesmith',
            'linkedin': 'https://linkedin.com/in/janesmith'
        }
    }
    
]

@app.route('/')
def home():
    return render_template('index.html', team_members=team_members)

